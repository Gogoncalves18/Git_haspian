# Aula 04 - Programador Lhama - https://youtu.be/SYXBWHPGRY4?si=fg9Mmls2L2nSvkWK
# Abertura do motor de conexao
from sqlalchemy import create_engine
# biblioteca para inserir comandos em txt sql
from sqlalchemy import text
from dotenv import load_dotenv
from os import getenv
# Importacao para fazer o mapping da tabela
from sqlalchemy.ext.declarative import declarative_base as dec_b
# Importacao da tipagem para declarar a tabela do SQL
from sqlalchemy import Column, String, Integer
# Importacao para controlar a sessao do ORM
from sqlalchemy.orm import sessionmaker as sm

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

# Instancia para especificar o mapping da tabela sql
Base = dec_b()
# Primeiro eu uso o sessionmaker para instaciar uma secao em Secao, imprtante entender
# que o bind dentro dela esta escutando a instancia da conexao, ao momento que ele
# instancia a conexao, ele desperta o session maker
Secao = sm(bind=conn)
# Depois passo o obj para uma outra instancia
secao = Secao()

# Em entidade vamos instanciar o mapping e declarar a estrutura da tabela do Script.sql

# Sempre devemos usar o nome da class igual ao nome da tabela que estamos 
# mapeando no sqlalchemy, dentro dela carregamos a herança do declarative base
class Filmes(Base):
    # Cmd para identificar para o alchemy que este mapping é da tabela filmes do BD
    __tablename__ = "filmes"

    # Especificacao das colunas
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    # Definicao de uma funcao para printar dados da tabela
    def __repr__(self):
        return f'Filme => (Titulo= {self.titulo} -- Ano= {self.ano})'
    

# Processos sql

# SELECT
# Execucao de um cmd sql é necessario pegar o seccionmaker e executar 
# sobre uma class que representa a tabela
data = secao.query(Filmes).all()
print(data)
print(data[0])
print(data[0].titulo)

# INSERT
# Monto um objeto da classe que representa a tabela no BD e dela 
# executo o comando de insert pelo alchemy
data_insert = Filmes(titulo="pegadinha", genero="Terror", ano=1998)
# Insiro o obj montada
secao.add(data_insert)
secao.commit()
secao.close()

# DELETE 
# Este cmd é feito pelo filtro do ORM com o .delete() no final
# aqui eu deleto apenas o filme que tem o nome Pegadinha
secao.query(Filmes).filter(Filmes.titulo == "Pegadinha").delete()
secao.commit()

# UPDATE
# No update além de fazer o filtro para, no update é necessário passar 
# o atributo de atualização dentro de dict
secao.query(Filmes).filter(Filmes.genero == "Terror").update({"ano": 2000})
secao.commit()

# SELECT
# Execucao de um cmd sql é necessario pegar o seccionmaker e executar 
# sobre uma class que representa a tabela
data = secao.query(Filmes).all()
print(data)
