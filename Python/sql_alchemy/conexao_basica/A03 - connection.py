# Aula 03 - Programador Lhama - https://youtu.be/r1OhZTYz4-Q?si=BEeNLDiQVqdH8U1p
# Abertura do motor de conexao
from sqlalchemy import create_engine
# biblioteca para inserir comandos em txt sql
from sqlalchemy import text
from dotenv import load_dotenv
from os import getenv

load_dotenv()
# Dados para conexao
user = getenv('user')
pw = getenv('pw')
server = getenv('server')
db = getenv('db')
driver = getenv('driver')
port = getenv('port')

# Conexao com usuario e senha no sql
str_db = f'mssql+pyodbc://{user}:{pw}@{server}/{db}?driver={driver}'

# Conexao com autenticacao do windows no sql
# str_db = f'mssql+pyodbc://{server}/{db}?Trusted_Connection=yes\\
# &driver={driver}'

# Motor que se encarrega de abrir e fechar a conexao
engine = create_engine(str_db)

# Instancia para conexao
conn = engine.connect()
if conn:
    print('>>> CONECTADO AO BD <<<')
    print(conn)
else:
    print('NÃO OCORREU A CONEXÃO AO BD')

# Formato para ler os dados atraves de cmds do SQL puro
with conn:
    resp = conn.execute(text("SELECT * FROM filmes"))
    for row in resp:
        print(row)
        print(row[1])
        print(row.titulo)
