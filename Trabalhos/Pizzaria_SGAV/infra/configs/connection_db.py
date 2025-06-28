# Classe para importacao do BD
from dotenv import load_dotenv
from os import getenv
# Criacao da engine
from sqlalchemy import create_engine, text
# Criacao da session do sql
from sqlalchemy.orm import sessionmaker as sm


class DBConnection:
    '''Classe para controle de multiBD's'''

    def __init__(self) -> None:
        # Importacao dos params
        self.__loader = self.load_init()
        # String de cnx montada
        self.__str_mssql = self.__loader
        # Abre a engine do sql
        self.__engine = self.__create_db_engine()
        # Controle de inicio automatico da session
        self.session = None

    def load_init(self) -> None:
        '''Carregamento dos dado do .env com
        as strings de conexão'''
        load_dotenv()
        self.user = getenv('userdb')
        self.pw = getenv('password')
        self.server = getenv('server')
        self.db = getenv('db_pdv')
        self.driver = getenv('driver')
        self.port = getenv('port')

        # String para conexao com o BD MSSQL
        str_db = f'mssql+pyodbc://{self.user}:{self.pw}@{self.server}/{self.db}?driver={self.driver}'
        return str_db

    def __create_db_engine(self) -> object:
        '''Controi uma engine sempre que a classe é instanciada.'''
        # Montagem da engine de conexao sob a str de conexao com o BD
        engine = create_engine(self.__str_mssql)
        # Devolve o obj de conexao pronto
        return engine

    def get_engine(self):
        '''Metodo para fazer cmds SQL puros'''
        return self.__engine

    def __enter__(self):
        # Este metodo é acionado automaticamente sempre que
        # a classe é instanciada, assim é construido a abertura
        # de uma sessao para o BD e ela só é aberta pq está
        # escutando se houve a construcao da engine, isto
        # atraves do "bind="
        session_make = sm(bind=self.__engine)
        # Instancio a sessao e devolvo ela para o contexto
        # da classe. Isto é, a classe tem uma sessao aberta
        # no atributo construtor "self.session"
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Sempre que a classe é usada, quando ele finaliza,
        este método mágico é evocado, assim uso ele para fechar
        a conexao com o BD'''
        self.session.close()


if __name__ == '__main__':
    conn = DBConnection()

    if conn:
        print('>>> CONECTADO AO BD <<<')
        print(conn)
    else:
        print('NÃO OCORREU A CONEXÃO AO BD')

    cmd = "SELECT * FROM modo_venda;"
    with DBConnection() as db:
        # data = db.session.execute(text('SELECT * FROM modo_venda;'))
        data = db.session.execute(text(cmd))
        print(data.fetchall())
