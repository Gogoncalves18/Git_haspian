from dotenv import load_dotenv
from os import getenv
import pyodbc
import pandas as pd


load_dotenv()

driver = getenv("driver")
server = getenv("server")
database = getenv("database")
username = getenv("username")
password = getenv("password")
tc = getenv("tc")

# String de conexao com o BD
str_conex = f"DRIVER={driver}; SERVER={server}; DATABASE={
                database}; UID={username}; PWD={
                password}; TRUSTED_CONNECTION={tc}"


def cons_sql():
    """
    Funcao para carregar o ID, OP e ACAO do BD.
    """
    conex = pyodbc.connect(str_conex)
    # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar os cmds
    cursor_sql = conex.cursor()
    cons_dados = "SELECT ID, OP, ACAO FROM dbo.testeSYNECO ORDER BY ID ASC;"

    try:
        # executa o cmd
        dados = cursor_sql.execute(cons_dados).fetchall()
        return dados

    except pyodbc.DatabaseError as avisos:
        print(f'PROBLEMA COM A MANIPULAÇÃO DO SQL\n:{avisos}')
        cursor_sql.rollback()
    finally:
        # linha de seguranca para o caso de dar tudo certo
        cursor_sql.close()


# Adicionar lista de itens do BD
def put_ofs(list_OP_bd):
    """
    Funcao que recebe um DataFrame e separa as conexoes com o BD
    em:
    INSERT -> Ao ler na coluna ACAO = 1;
    DELETE -> Ao ler na coluna ACAO = 2;
    UPDATE -> Ao ler na coluna ACAO = 3;

    Como resultado ela retorna:
    RETURN = 0 -> Para insucesso da transação no BD
    RETURN = 1 -> Para sucesso da transação no BD
    """
    df_trat = pd.DataFrame(list_OP_bd)
    # Variaveis para executar os cmd de BD com o PYODBC
    lista_ofs_insert = []
    lista_ofs_update = []
    lista_ofs_delete = []
    # Variavel controladora do commit com o BD
    data_recorded = 0
    # Separacao dos DataFrames por tipo de acao, derivo do DF recebido
    # para gerar novos DFs, como se fosse um Select Where no BD
    df_insert = df_trat[df_trat['ACAO'] == 1]
    df_delete = df_trat[df_trat['ACAO'] == 2]
    df_update = df_trat[df_trat['ACAO'] == 3]

    # Condicao para quando nao ha mudanca de itens na tabela
    if not df_trat.empty:
        conex = pyodbc.connect(str_conex)
        # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar
        # os cmds
        cursor_sql = conex.cursor()
        ins_sql = "INSERT INTO testeSYNECO VALUES (?, ?, ?, ?, ?)"
        up_sql = "UPDATE testeSYNECO SET OPER=?, DESCOPER=?, DateRegist=?, ACAO=? WHERE op=?"
        del_sql = "DELETE from testeSYNECO WHERE OP=?"

        # Valida se o DF esta vazio, caso contrario o PYODBC gera um aviso
        if not df_insert.empty:
            for i, raw in df_insert.iterrows():
                # val = (raw['OP'], raw['OPER'], raw['DESCOPER'], raw['DATEREGIST'], raw['ACAO'], raw['STATUS'])
                # ins_sql = "INSERT INTO testeSYNECO VALUES (?, ?, ?, ?, ?, ?)"

                # Guardo em uma variavel uma tupla de dados para executar
                # o cmd do PYODBC
                val = (raw['OP'], raw['OPER'], raw['DESCOPER'], raw['DATEREGIST'], raw['ACAO'])
                lista_ofs_insert.append(val)

        if not df_update.empty:
            for i, raw in df_update.iterrows():
                val_up = (raw['OPER'], raw['DESCOPER'], raw['DATEREGIST'], raw['ACAO'], raw['OP'])
                lista_ofs_update.append(val_up)

        if not df_delete.empty:
            for i, raw in df_delete.iterrows():
                # O cmd do PYODBC so funciona com tupla, neste caso como
                # somente um valor, precisamos usar ',' no final do dado
                # e entre parenteses
                val_del = (raw['OP'],)
                lista_ofs_delete.append(val_del)

        try:
            # Depois de guardar todos os dados que serao utilizados para
            # execucao do cmd, executamos um por um para dar a chance de
            # validar a falha e entao devolver que a conexao se rompeu e
            # os dados nao forma consolidados em BD. Considerado que a
            # variavel precisa ao menos ter um dado dentro dela
            if len(lista_ofs_insert) > 0:
                cursor_sql.executemany(ins_sql, lista_ofs_insert)
            if len(lista_ofs_update) > 0:
                cursor_sql.executemany(up_sql, lista_ofs_update)
            if len(lista_ofs_delete) > 0:
                cursor_sql.executemany(del_sql, lista_ofs_delete)
            conex.commit()
            # Flag a variavel que dira que gravamos todos os dados
            data_recorded = 1
        except pyodbc.DatabaseError as avisos:
            # print da saida de erro
            print(f'Aconteceu um ERRO ==>>> {avisos}')
            # cancelamento dos dados enviado no bd
            conex.rollback()
            data_recorded = 0
        finally:
            conex.close()
            return data_recorded


if __name__ == '__main__':
    lista = ['1011', '1010']
