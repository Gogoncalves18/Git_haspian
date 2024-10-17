from dotenv import load_dotenv
from os import getenv
import os
import pandas as pd
import pyodbc


load_dotenv()


def con_sql(driver, server, db, username, pw, tc):
    str_conex = f"DRIVER={driver}; SERVER={server}; DATABASE={
                db}; UID={username}; PWD={
                pw}; TRUSTED_CONNECTION={tc}"
    
    conex = pyodbc.connect(str_conex)
    # Abro um funcao da biblioteca, CURSOR() e instancio ela para usar os cmds
    cursor_sql = conex.cursor()
    # Em variaveis monto os mesmos scripts do sql mantendo "" por fora e
    # simples por dentro
    cmd_cons = "select TOP (10) * from dbo.SSPImport"
    # Recomendado abrir um try para controla insucessos no BD e tambem fechar
    # as conexoes abertas por cada cursor que executo
    try:
        # EXECUTE() e cmd do cursor que esta instanciado e nele eu devo passar
        # o script sql. O FETCHALL() neste caso e para atacar todas as linhas
        # da consulta
        inf = cursor_sql.execute(cmd_cons).fetchall()
        # Se o BD estiver sem registro, ele volta para mim uma []
        # senao voltara uma [(datetime.date(2024, 8, 27),)]
        
        return inf
    # pyodbc.DatabaseError e onde recebo os erros das tratativas no SQL
    except pyodbc.DatabaseError as avisos:
        print(f'MENSAGEM DO SQL APOS INSUCESSO:\n\n{avisos}\n')
        # Sempre devemos aplicar um ROLLBACK() no PYODBC apos um insucesso
        conex.rollback()
    finally:
        # Por fim devo sempre fechar a conexao aberta pelo CURSOR()
        conex.close()


xls = getenv("table")
xls_path = getenv("loc_xls")
xls_imported = os.path.join(xls_path, xls)


driver = getenv("driver")
server = getenv("server")
database = getenv("database")
username = getenv("username")
password = getenv("password")
tc = getenv("tc")

#df_xls(xls_imported)

dados = con_sql(driver, server, database, username, password, tc)