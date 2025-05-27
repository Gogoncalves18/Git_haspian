'''Na pasta de repository é reservado os foco dos cmds sql
a partir daqui é importado o ambiente de conexao com o BD,
DBConnection que possui as str de conexao. Importo tambem
as tabelas que pretendo gerar as consultas'''
from infra.configs.connection_db import DBConnection
from infra.entities_bd.atores import Atores

# Importo filmes aqui dentro para poder fazer um join de tabelas
from infra.entities_bd.filmes import Filmes

class Atores_Repository:
    '''Classe responsável em gerar os comandos SQL para
    acesso ao BD através da ORM SQLAlchemy'''
    def select(self) -> list:
        '''Retorno de uma lista de instancias dentro da tabela
        Filmes do Banco de dados.'''
        # Com o DBConnection e o cmd with, eu consigo gerar um
        # tipo de instancia que me retorna a conexao do BD com
        # a sessão aberta até finalizar a execução do comando.
        # Com esta sessão, é possível buscar os cmds do Alchemy
        with DBConnection() as db:
            # Da conexão eu chamo a sessão e depois os cmds
            # A importacao de filmes define o mapping de BD que
            # estou fazendo
            '''Abro o join aqui dentro para unir com outra tabela.
            Com o ".with_entities" eu consigo cruzar os dados das
            tabela "(Atores, Filmes)"'''
            data = db.session.query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                    Atores.nome,
                    Filmes.genero,
                    Filmes.titulo)\
                .all()
            return data
