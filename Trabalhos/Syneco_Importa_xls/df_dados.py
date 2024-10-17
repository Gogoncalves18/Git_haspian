from dotenv import load_dotenv
from os import getenv
import os
import pandas as pd
from conex_db import put_ofs


load_dotenv()

xls = getenv("table")
xls_path = getenv("loc_xls")
xls_imported = os.path.join(xls_path, xls)


def df_xls(lista_op_bd):
    """
    Funcao recebe uma lista de OPs que existem no BD
    para compara-las com o que sera lido em tabela excel.
    Ela devolve um pacote de dados:

    df_ofs_final -> Um dataframe completo do que foi inserido em BD
    tanto com o INSERT, UPDATE e DELETE.

    data_recorded -> valor 0 para insucesso nos dados do "df_ofs_final"
    ou 1 para sucesso nos dados no BD.

    Esta fx() ou consolida todos os movimentos, ou nao consolida nada do DF.
    """
    # Leitura do excel
    df_ofs = pd.read_excel(xls_imported)

    # Tratamento das series de dados (colunas) do DataFrame
    df_ofs['OP'] = df_ofs['OP'].astype('Int64')
    df_ofs['OPER'] = df_ofs['OPER'].astype('Int64')
    df_ofs['DESCOPER'] = df_ofs['DESCOPER'].astype('object')
    df_ofs['ACAO'] = df_ofs['ACAO'].astype('Int64')
    df_ofs['STATUS'] = df_ofs['STATUS'].astype('int')
    # Forma de transformar a data texto em data para o SQL
    pd.to_datetime(df_ofs['DATEREGIST'])

    '''
    Para conseguir enviar um dado NULL para o sql e necessário carregar
    o DataFrame, chamar o tipo do objetos dentro dele e executar o where.
    Cuidado, where() do pandas e igual ao mask(), o mask faz a mesma coisa
    que outros Where, ja o where do pandas busca a funcao contraria.
    Por isto passamos no pd.notnull(df_ofs), para buscar todos valores NaN,
    dentro do DF e retornar None, desta forma ele enviara NULL para o SQL.

    Ja a forma de colocar uma coluna como None para valores NaN:
        df_ofs['DESCOPER'] = df_ofs['DESCOPER'].fillna(value=None)
    so funciona se passarmos um texto, este caso acima ele gerara uma
    string vazia para o SQL.
    '''

    df_ofs = df_ofs.astype(object).where(pd.notnull(df_ofs), None)
    # Comprimento da coluna de OP de dados do DF para fazer o laco for
    tam_col = len(df_ofs['OP'])
    # Indice para saber qual linha do excel estou para entao saber
    # qual fatia considerarei para inserir no BD
    indice = 0

    for i in range(0, tam_col):
        if df_ofs['OP'][i] in lista_op_bd:
            indice += 1
            # print(f'====>>>> Achei a OP {df_ofs['OP'][i]}')

    # Fatiamento do DF para envio para o BD
    # Todas OF novas
    df_ofs_news = df_ofs[indice:]
    # Todas OF's que precisarei atualizar, o '|' faz o OU do select que
    # estou fazendo no DF e preciso colocar entre () para funcionar a condicao
    df_ofs_updated = df_ofs[(df_ofs['ACAO'] == 2) | (df_ofs['ACAO'] == 3)]

    # CONCAT dos dois DF e opcao para refazer um index do DF
    df_ofs_final = pd.concat([df_ofs_news, df_ofs_updated], ignore_index=True)
    # Envia somente o DF que precisa inserir, atualizar ou deletar no BD e
    # retorna 0 ou 1 para insucesso ou sucesso
    data_recorded = put_ofs(df_ofs_final)
    return df_ofs_final, data_recorded


if __name__ == '__main__':
    lst = [1000, 1001, 1003, 1004, 1005]
    print(df_xls(lst))
