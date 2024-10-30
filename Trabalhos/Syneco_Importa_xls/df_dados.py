from dotenv import load_dotenv
from os import getenv
import os
import pandas as pd
from conex_db import put_ofs
import datetime
import numpy as np


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
    df_ofs = pd.read_excel(xls_imported,  sheet_name="SSPImport")
    df_PC_OPS = pd.read_excel(xls_imported,  sheet_name="pcs_OPS")

    df_OF_Full = df_ofs.merge(df_PC_OPS)
    pd.set_option('display.max_columns', None)

    # Fatia o DF removendo todas as linhas da coluna arranjos que estao
    # vazias, "~df_arranjos" o '~' indica o contrario para o pandas, sendo
    # assim, retornara todas linhas que sao contrarias ao .isnull()
    df_OF_Full = df_OF_Full[~df_OF_Full['OF'].isnull()]

    df_OF_Full['OF'] = df_OF_Full['OF'].astype('Int64')
    df_OF_Full['CODPECA'] = df_OF_Full['CODPECA'].astype('object')
    df_OF_Full['DESCPECA'] = df_OF_Full['DESCPECA'].astype('object')
    df_OF_Full['PLANQTY'] = df_OF_Full['PLANQTY'].astype('Int64')
    df_OF_Full['ACAO'] = df_OF_Full['ACAO'].astype('int')
    df_OF_Full['OPER'] = df_OF_Full['OPER'].astype('Int64')
    df_OF_Full['SEQOPER'] = df_OF_Full['SEQOPER'].astype('Int64')
    df_OF_Full['DESCOPER'] = df_OF_Full['DESCOPER'].astype('object')
    df_OF_Full['QTD_CICLO'] = df_OF_Full['QTD_CICLO'].astype('int')
    df_OF_Full['PLANTMUNIT'] = df_OF_Full['PLANTMUNIT'].astype('Float64')
    df_OF_Full['PLANTMSETUP'] = df_OF_Full['PLANTMSETUP'].astype('Float64')
    df_OF_Full['PRODAUX1'] = df_OF_Full['PRODAUX1'].astype('object')
    df_OF_Full['PRODAUX2'] = df_OF_Full['PRODAUX2'].astype('object')
    df_OF_Full['PRODAUX3'] = df_OF_Full['PRODAUX3'].astype('object')
    df_OF_Full['PRODAUX4'] = df_OF_Full['PRODAUX4'].astype('object')

    df_OF_Full.insert(loc=15, column='DATEREGIST',
                      value=datetime.datetime.today())
    df_OF_Full.insert(loc=16, column='ISENABLE', value=1)
    df_OF_Full.insert(loc=17, column='PARENTID', value=np.nan_to_num(None))

    df_OF_Full['PARENTID'] = df_OF_Full['PARENTID'].astype('Int64')

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

    df_OF_Full = df_OF_Full.astype(object).where(pd.notnull(df_OF_Full), None)
    # df_OF_Full = df_OF_Full.astype(object).where(pd.notnull(df_OF_Full),
    #                                               None)
    print(df_OF_Full)
    df_OF_Full.info()

    # Comprimento da coluna de OP de dados do DF para fazer o laco for
    tam_col = len(df_OF_Full['OF'])
    # Indice para saber qual linha do excel estou para entao saber
    # qual fatia considerarei para inserir no BD
    indice = 0

    for i in range(0, tam_col):
        # inf = df_OF_Full['OF'][i]
        if str(df_OF_Full['OF'][i]) in lista_op_bd:
            indice += 1
            # print(f'====>>>> Achei a OP {df_OF_Full['OF'][i]}')
    # Fatiamento do DF para envio para o BD
    # Todas OF novas
    df_ofs_news = df_OF_Full[indice:]
    # Todas OF's que precisarei atualizar, o '|' faz o OU do select que
    # estou fazendo no DF e preciso colocar entre () para funcionar a condicao
    df_ofs_updated = df_OF_Full[(df_OF_Full['ACAO'] == 2) |
                                (df_OF_Full['ACAO'] == 3)]
    df_ofs_updated.info()
    # CONCAT dos dois DF e opcao para refazer um index do DF
    df_ofs_final = pd.concat([df_ofs_news, df_ofs_updated], ignore_index=True)
    df_ofs_final.info()
    # Envia somente o DF que precisa inserir, atualizar ou deletar no BD e
    # retorna 0 ou 1 para insucesso ou sucesso
    data_recorded = put_ofs(df_ofs_final, 'xls')
    return df_ofs_final, data_recorded


def df_nest(lista_op_bd):
    df_arranjos = pd.read_excel(xls_imported,  sheet_name="Arranjos")

    pd.set_option('display.max_columns', None)

    df_arranjos['ARRANJOS'] = df_arranjos['ARRANJOS'].astype('object')      #1
    df_arranjos['CODPECA'] = df_arranjos['CODPECA'].astype('object')        #2
    df_arranjos['DESCPECA'] = df_arranjos['DESCPECA'].astype('object')      #3
    df_arranjos['QTD_PC'] = df_arranjos['QTD_PC'].astype('Int64')           #4
    df_arranjos['ACAO'] = df_arranjos['ACAO'].astype('Int64')               #5
    df_arranjos.insert(loc=6, column='OPER', value=np.nan_to_num(None))     #6
    df_arranjos.insert(loc=7, column='SEQ', value=np.nan_to_num(None))      #7
    df_arranjos.insert(loc=8, column='DESCOPER', value='Nesting')           #8
    df_arranjos['QTD_CHAPA'] = df_arranjos['QTD_CHAPA'].astype('Int64')     #9
    df_arranjos.insert(loc=10, column='PLANTMUNIT',
                       value=np.nan_to_num(None))                           #10
    df_arranjos.insert(loc=11, column='PLANTMSETUP',
                       value=np.nan_to_num(None))                           #11
    df_arranjos.insert(loc=12, column='PRODAUX1',
                       value=None)                                          #12
    df_arranjos.insert(loc=13, column='PRODAUX2',
                       value=None)                                          #13
    df_arranjos.insert(loc=14, column='PRODAUX3',
                       value=None)                                          #14
    df_arranjos.insert(loc=15, column='PRODAUX4',
                       value=None)                                          #15

    df_arranjos.insert(loc=16, column='DATEREGIST',
                       value=datetime.datetime.today())                     #16

    df_arranjos.insert(loc=17, column='ISENABLE', value=1)                  #17

    df_arranjos.insert(loc=18, column='PARENTID',
                       value=np.nan_to_num(None))                           #18

    # Para controlar qual OF inativar
    df_arranjos['OF'] = df_arranjos['OF'].astype('object')                   

    df_arranjos['OPER'] = df_arranjos['OPER'].astype('Int64')
    df_arranjos['SEQ'] = df_arranjos['SEQ'].astype('Int64')
    df_arranjos['PLANTMUNIT'] = df_arranjos['PLANTMUNIT'].astype('Int64')
    df_arranjos['PLANTMSETUP'] = df_arranjos['PLANTMSETUP'].astype('Int64')
    df_arranjos['PARENTID'] = df_arranjos['PARENTID'].astype('Int64')

    # Fatia o DF removendo todas as linhas da coluna arranjos que estao
    # vazias, "~df_arranjos" o '~' indica o contrario para o pandas, sendo
    # assim, retornara todas linhas que sao contrarias ao .isnull()
    df_arranjos = df_arranjos[~df_arranjos['ARRANJOS'].isnull()]

    df_arranjos = df_arranjos.astype(object).where(pd.notnull(df_arranjos), None)
    # print(df_arranjos)

    # Comprimento da coluna de OP de dados do DF para fazer o laco for
    tam_col = len(df_arranjos['ARRANJOS'])

    # Indice para saber qual linha do excel estou, para entao saber
    # qual fatia considerarei para inserir no BD
    indice = 0

    for i in range(0, tam_col):
        if df_arranjos['ARRANJOS'][i] in lista_op_bd:
            indice += 1
            # print(f'====>>>> Achei a OP {df_OF_Full['OF'][i]}')
    # Fatiamento do DF para envio para o BD
    # Todas OF novas
    df_ofs_news = df_arranjos[indice:]
    # Todas OF's que precisarei atualizar, o '|' faz o OU do select que
    # estou fazendo no DF e preciso colocar entre () para funcionar a condicao
    df_ofs_updated = df_arranjos[(df_arranjos['ACAO'] == 2) |
                                 (df_arranjos['ACAO'] == 3)]

    # CONCAT dos dois DF e opcao para refazer um index do DF
    df_ofs_final = pd.concat([df_ofs_news, df_ofs_updated], ignore_index=True)
    # Envia somente o DF que precisa inserir, atualizar ou deletar no BD e
    # retorna 0 ou 1 para insucesso ou sucesso

    data_recorded = put_ofs(df_ofs_final, 'nest')
    return df_ofs_final, data_recorded


if __name__ == '__main__':
    lst = [1000, 1001, 1003, 1004, 1005]
    df_xls(lst)
