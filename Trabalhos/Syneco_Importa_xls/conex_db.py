from dotenv import load_dotenv
from os import getenv
import pyodbc
import pandas as pd
import datetime


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


def val_sql():
    use_db = f"USE {database}"
    use_tb = "select * from pilotoSYNECO"
    create_tb = "create table pilotoSYNECO (\
                ID int not null Identity(1,1),\
	            ODF nvarchar(32) not null,\
                CODPECA nvarchar(32) null,\
                DESCPECA nvarchar(120),\
                PLANQTY int null,\
                ACAO INT not null,\
                OPER INT null,\
                SEQOPER INT null,\
                DESCOPER nvarchar(50),\
                QTD_CICLO INT not null,\
                PLANTMUNIT REAL,\
                PLANTMSETUP REAL,\
                PRODAUX1 nvarchar(200) null,\
                PRODAUX2 nvarchar(200) null,\
                PRODAUX3 nvarchar(200) null,\
                PRODAUX4 nvarchar(200) null,\
                DATEREGIST datetime not null,\
                ISENABLE int not null,\
                PARENTID int null\
                )"

    try:
        conex = pyodbc.connect(str_conex)
        conex_ok = True
        cursor_sql = conex.cursor()
        conex.autocommit = True
        if conex_ok is True:
            cursor_sql.execute(use_db)
        tabs = []
        for t in cursor_sql.tables():
            tabs.append(t.table_name)
        if tabs[0] == 'pilotoSYNECO':
            return 1, 'DBO.pilotoSYNECO existente.'
        else:
            cursor_sql.execute(create_tb)
            return 2, 'DBO.pilotoSYNECO criado.'

    except pyodbc.Error as msg:
        return 0, msg
    finally:
        # linha de seguranca para o caso de dar tudo certo
        cursor_sql.close()


def cons_sql():
    """
    Funcao para carregar o ID, OP e ACAO do BD.
    """
    conex = pyodbc.connect(str_conex)
    # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar os cmds
    cursor_sql = conex.cursor()
    cons_dados = "SELECT ID, ODF, ACAO FROM dbo.pilotoSYNECO ORDER BY ID ASC;"

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
def put_ofs(list_OP_bd, nome_df, list_ofs=0, nestings=0):
    """
    Funcao que recebe um DataFrame e separa as conexoes com o BD
    em:
    INSERT -> Ao ler na coluna ACAO = 1;
    DELETE -> Ao ler na coluna ACAO = 2;
    UPDATE -> Ao ler na coluna ACAO = 3;

    Recebe no segundo parâmetro no nome do DF para tratamento:
    'xls' -> Para inserir os dados de OF do Excel
    'nest' -> Para inserir os dados nesting do Excel
    'nest' -> Para inserir os dados nesting do Excel
    'OfDeact' -> Para desativar as OF's que foram replicadas

    Recebe no terceiro parâmetro:
    0 -> Para desconsiderar uma lista de OFS de referência
    List[] -> Para considerar uma lista de OFS de referência

    Recebe no quarto parâmetro:
    0 -> Para desconsiderar uma lista de Nestings de referência
    List[] -> Para considerar uma lista de Nestings de referência

    Como resultado ela retorna:
    RETURN = 0 -> Para insucesso da transação no BD
    RETURN = 1 -> Para sucesso da transação no BD
    """
    df_trat = pd.DataFrame(list_OP_bd)
    # Variaveis para executar os cmd de BD com o PYODBC
    lista_ofs_insert = []
    lista_ofs_update = []
    lista_ofs_deactive = []
    lista_ofs_delete = []
    lista_nestings = []
    list_parent = []
    lista_ofs_update_nest = []
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
        ins_sql = "INSERT INTO pilotoSYNECO VALUES (?, ?, ?,\
                                                    ?, ?, ?,\
                                                    ?, ?, ?,\
                                                    ?, ?, ?,\
                                                    ?, ?, ?,\
                                                    ?, ?, ?)"

        if nome_df == 'xls':
            up_sql = "UPDATE pilotoSYNECO SET CODPECA=?, DESCPECA=?, PLANQTY=?,\
                                        ACAO=?, OPER=?, SEQOPER=?,\
                                        DESCOPER=?, QTD_CICLO=?, PLANTMUNIT=?,\
                                        PLANTMSETUP=?, PRODAUX1=?, PRODAUX2=?,\
                                        PRODAUX3=?, PRODAUX4=?, DATEREGIST=?,\
                                        ISENABLE=?, PARENTID=? WHERE ODF=?"
        elif nome_df == 'nest':
            up_sql = "UPDATE pilotoSYNECO SET PLANQTY=?, ACAO=?, DATEREGIST=?\
                                        WHERE ODF=? AND OPER IS NULL"
            
            up_nest_sql = "UPDATE pilotoSYNECO SET PLANQTY=?, ACAO=?, OPER=?, SEQOPER=?,\
                                        QTD_CICLO=?, DATEREGIST=?, ISENABLE=?\
                                        WHERE ODF=? AND OPER=20"

        del_sql = "DELETE from pilotoSYNECO WHERE ODF=?"

        deactive_sql = "UPDATE pilotoSYNECO SET ISENABLE=? WHERE ODF=? AND OPER=20"

        parent_sql = "UPDATE pilotoSYNECO SET PARENTID=\
            (select id from pilotoSYNECO where ODF=? and OPER=20)\
             where ODF=? AND OPER IS NULL"

        # Valida se o DF esta vazio, caso contrario o PYODBC gera um aviso
        if not df_insert.empty:
            if nome_df == 'xls':
                for i, raw in df_insert.iterrows():
                    # Guardo em uma variavel uma tupla de dados para executar
                    # o cmd do PYODBC
                    val = (raw['OF'], raw['CODPECA'], raw['DESCPECA'],
                           raw['PLANQTY'], raw['ACAO'], raw['OPER'],
                           raw['SEQOPER'], raw['DESCOPER'], raw['QTD_CICLO'],
                           raw['PLANTMUNIT'], raw['PLANTMSETUP'], raw['PRODAUX1'],
                           raw['PRODAUX2'], raw['PRODAUX3'], raw['PRODAUX4'],
                           raw['DATEREGIST'], raw['ISENABLE'], raw['PARENTID'])
                    lista_ofs_insert.append(val)
            elif nome_df == 'nest':
                for i, raw in df_insert.iterrows():
                    # Guardo em uma variavel uma tupla de dados para executar
                    # o cmd do PYODBC
                    val = (raw['ARRANJOS'], raw['CODPECA'], raw['DESCPECA'],
                           raw['QTD_PC'], raw['ACAO'], raw['OPER'],
                           raw['SEQ'], raw['DESCOPER'], raw['QTD_CHAPA'],
                           raw['PLANTMUNIT'], raw['PLANTMSETUP'], raw['PRODAUX1'],
                           raw['PRODAUX2'], raw['PRODAUX3'], raw['PRODAUX4'],
                           raw['DATEREGIST'], raw['ISENABLE'], raw['PARENTID'])
                    lista_ofs_insert.append(val)

        if not df_update.empty:
            if nome_df == 'xls':
                for i, raw in df_update.iterrows():
                    val_up = (raw['CODPECA'], raw['DESCPECA'], raw['PLANQTY'],
                              raw['ACAO'], raw['OPER'], raw['SEQOPER'],
                              raw['DESCOPER'], raw['QTD_CICLO'], raw['PLANTMUNIT'],
                              raw['PLANTMSETUP'], raw['PRODAUX1'], raw['PRODAUX2'],
                              raw['PRODAUX3'], raw['PRODAUX4'], raw['DATEREGIST'],
                              raw['ISENABLE'], raw['PARENTID'], str(raw['OF']))
                    lista_ofs_update.append(val_up)
            elif nome_df == 'nest':
                for i, raw in df_update.iterrows():
                    val_up = (raw['QTD_PC'],
                              raw['ACAO'],
                              raw['DATEREGIST'],
                              str(raw['ARRANJOS']))
                    val_nest_up = (str(raw['QTD_CHAPA']), raw['ACAO'], 20,
                                   1, 1, raw['DATEREGIST'],
                                   raw['ISENABLE'], str(raw['ARRANJOS']))
                    lista_ofs_update.append(val_up)
                    lista_ofs_update_nest.append(val_nest_up)

        # Atualiza o campo de OPS ISENABLE para ativar ou desativar Ops que 
        # foram replicadas por causa dos nestings
        if list_ofs != 0 and nome_df == 'OfDeact':            
            for i in list_ofs:
                for ind, raw in df_insert.iterrows():
                    if i == str(int(raw['OF'])):
                        val_up = (0, i)
                        lista_ofs_deactive.append(val_up)

        # Insere os arranjos como chapa e associa as OFs que compoem estes
        # arranjos pelo ParentID
        if nestings != 0 and nome_df == 'OfDeact':
            for i in nestings:
                date_reg = datetime.datetime.today()
                qtd_chapa = list(set(df_trat.loc[df_trat['ARRANJOS'] == i,
                                                 'QTD_CHAPA']))[0]
                val_up = (i, f'Nesting {i}', None,
                          qtd_chapa, 1, 20,
                          1, 'Nesting', 1,
                          None, None, None,
                          None, None, None,
                          date_reg, 1, None)
                val_parent = (i, i)
                lista_nestings.append(val_up)
                list_parent.append(val_parent)

        if not df_delete.empty:
            for i, raw in df_delete.iterrows():
                # O cmd do PYODBC so funciona com tupla, neste caso como
                # somente um valor, precisamos usar ',' no final do dado
                # e entre parenteses
                val_del = (raw['OF'],)
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
                if nome_df == 'nest':
                    cursor_sql.executemany(up_sql, lista_ofs_update)
                    cursor_sql.executemany(up_nest_sql, lista_ofs_update_nest)
                else:
                    cursor_sql.executemany(up_sql, lista_ofs_update)
            if len(lista_ofs_delete) > 0:
                cursor_sql.executemany(del_sql, lista_ofs_delete)
            if len(lista_ofs_deactive) > 0:
                cursor_sql.executemany(deactive_sql, lista_ofs_deactive)
            if len(lista_nestings) > 0:
                cursor_sql.executemany(ins_sql, lista_nestings)
                cursor_sql.executemany(parent_sql, list_parent)
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
    val_sql()
