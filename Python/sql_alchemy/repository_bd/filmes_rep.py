'''Na pasta de repository é reservado os foco dos cmds sql
a partir daqui é importado o ambiente de conexao com o BD,
DBConnection que possui as str de conexao. Importo tambem
as tabelas que pretendo gerar as consultas'''
from infra.configs.connection_db import DBConnection
from infra.entities_bd.filmes import Filmes
# Importacao da biblioteca para tratar erros no sql alchemy
from sqlalchemy.orm.exc import NoResultFound


class Filmes_Repository:
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
            '''Tratamento de erro no alchemy'''
            try:
                data = db.session.query(Filmes).all()
                return data
            except NoResultFound:
                return None

    def insert(self, titulo: str, genero: str, ano: int) -> None:
        # Monto um objeto da classe que representa a tabela no BD e dela
        # executo o comando de insert pelo alchemy
        with DBConnection() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                # Insiro o obj montada
                db.session.add(data_insert)
                db.session.commit()
            except Exception as err:
                # Desfaco as operacoes realizadas até o momento
                db.session.rollback()
                raise err

    def delete(self, titulo: str) -> None:
        # Monto um objeto da classe que representa a tabela no BD e dela
        # executo o comando de insert pelo alchemy
        with DBConnection() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
                db.session.commit()
            except Exception as err:
                db.session.rollback()
                raise err

    def update(self, titulo: str, ano: int) -> None:
        # Monto um objeto da classe que representa a tabela no BD e dela 
        # executo o comando de insert pelo alchemy
        with DBConnection() as db:
            try:
                db.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
                db.session.commit()
            except Exception as err:
                db.session.rollback()
                raise err