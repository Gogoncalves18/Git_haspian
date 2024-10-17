from dotenv import load_dotenv
from os import getenv
import os
import pandas as pd
import pyodbc
import numpy as np
import datetime


load_dotenv()


xls = getenv("table")
xls_path = getenv("loc_xls")
xls_imported = os.path.join(xls_path, xls)


driver = getenv("driver")
server = getenv("server")
database = getenv("database")
username = getenv("username")
password = getenv("password")
tc = getenv("tc")


def con_sql(driver, server, db, username, pw, tc):
    str_conex = f"DRIVER={driver}; SERVER={server}; DATABASE={
                db}; UID={username}; PWD={
                pw}; TRUSTED_CONNECTION={tc}"

    conex = pyodbc.connect(str_conex)
    # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar os cmds
    cursor_sql = conex.cursor()

    df_sql = df_xls(xls_imported)
    # df_sql.info()  # Retorna infos gerais do DF
    # print(df_sql.isna().any())  # Return bool para NaN(Null) para coluna
    # print(df_sql.isnull().any())  # Return bool para NaN(Null) para colun
    # print(df_sql.isna().sum())  # Return contagem de NaN para Coluna
    # print(df_sql)

    dados_df = []
    for index, row in df_sql.iterrows():
        # cmd_sql = "INSERT INTO SSPImport (OP, OPER, SEQOPER, DESCOPER, CODPECA, DESCPECA, PRODAUX1, PRODAUX2, PRODAUX3, PRODAUX4, MAQ, CENTROCUSTO, PLANDTINI, PLANHRINI, PLANDTFIM, PLANHRFIM, PLANQTY, CYCLEQTY, PLANTMUNIT, PLANTMSETUP, ACAO, STATUS, DateRegist, DateProcess) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cmd_sql = "INSERT INTO testeSYNECO VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        # cmd_sql = "INSERT INTO testeSYNECO VALUES (?, ?, ?, ?, ?)"
        val = (row['OF'], row['OPER'], row['SEQOPER'], row['DESCOPER'], row['CODPECA'], row['DESCPECA'], row['PRODAUX1'], row['PRODAUX2'], row['PRODAUX3'], row['PRODAUX4'], row['MAQ'], row['CENTROCUSTO'], row['PLANDTINI'], row['PLANHRINI'], row['PLANDTFIM'], row['PLANHRFIM'], row['PLANQTY'], row['CYCLEQTY'], row['PLANTMUNIT'], row['PLANTMSETUP'], row['ACAO'], row['STATUS'], row['DATEREGIST'], row['DATEPROCESS'])
        # val = (row['OF'], row['OPER'], row['DESCOPER'], row['CODPECA'], row['DESCPECA'])
        
        dados_df.append(val)

    try:
        cursor_sql.executemany(cmd_sql, dados_df)
        # while cursor_sql.nextset():
            #pass
        conex.commit()
    except pyodbc.DatabaseError as avisos:
        # print da saida de erro
        print(f'Aconteceu um ERRO ==>>> {avisos}')
        # cancelamento dos dados enviado no bd
        conex.rollback()
    finally:    
        conex.close()
    print(dados_df)

def df_xls(xls_imported):
    df_ofs = pd.read_excel(xls_imported)
    df_OPS = pd.read_excel(xls_imported,  sheet_name="pcs_OPS")

    tab_Completa = df_ofs.merge(df_OPS)

    tab_Completa.insert(loc=0, column='MAQ', value='')
    tab_Completa.insert(loc=1, column='CENTROCUSTO', value='')
    tab_Completa.insert(loc=2, column='PLANDTINI', value='')
    tab_Completa.insert(loc=3, column='PLANHRINI', value='')
    tab_Completa.insert(loc=4, column='PLANDTFIM', value='')        
    tab_Completa.insert(loc=5, column='PLANHRFIM', value='')
    tab_Completa.insert(loc=6, column='CYCLEQTY', value=1)
    tab_Completa.insert(loc=7, column='STATUS', value=0)
    tab_Completa.insert(loc=8, column='DATEREGIST', value=datetime.datetime.today())
    tab_Completa.insert(loc=9, column='DATEPROCESS', value='')

    tab_Completa['OF'] = tab_Completa['OF'].astype('object')
    tab_Completa['CODPECA'] = tab_Completa['CODPECA'].astype('object')
    tab_Completa['DESCPECA'] = tab_Completa['DESCPECA'].astype('object')
    tab_Completa['PLANQTY'] = tab_Completa['PLANQTY'].astype('Int64')
    tab_Completa['ACAO'] = tab_Completa['ACAO'].astype('Int64')
    tab_Completa['OPER'] = tab_Completa['OPER'].astype('object')
    tab_Completa['SEQOPER'] = tab_Completa['SEQOPER'].astype('Int64')
    tab_Completa['DESCOPER'] = tab_Completa['DESCOPER'].astype('object')
    tab_Completa['PLANTMUNIT'] = tab_Completa['PLANTMUNIT'].astype('Float64')
    tab_Completa['PLANTMSETUP'] = tab_Completa['PLANTMSETUP'].astype('Float64')
    tab_Completa['PRODAUX1'] = tab_Completa['PRODAUX1'].astype('object')
    tab_Completa['PRODAUX2'] = tab_Completa['PRODAUX2'].astype('object')
    tab_Completa['PRODAUX3'] = tab_Completa['PRODAUX3'].astype('object')
    tab_Completa['PRODAUX4'] = tab_Completa['PRODAUX4'].astype('object')
    # tab_Completa.info()
    # print(f'\n{tab_Completa}')
    return tab_Completa


dados = con_sql(driver, server, database, username, password, tc)
