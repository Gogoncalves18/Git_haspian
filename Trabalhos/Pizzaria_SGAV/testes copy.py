from modulos.conexao_bds import ConectorBD
from modulos.crud_bd import RepositorioBD
from dotenv import load_dotenv
from os import getenv

load_dotenv()

driver = getenv('driver')
server = getenv('server')
db_pdv = getenv('db_pdv')
username = getenv('username')
password = getenv('password')
tc = getenv('tc')
bak_sql_pdv = getenv("bak_sql_pdv")

conn_bd_pdv = ConectorBD(driver, server, db_pdv, username, password, tc)
acoes = RepositorioBD(conn_bd_pdv)
print(acoes)
acoes.

