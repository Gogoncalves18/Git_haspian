# Classe para conexao do BD
# Importacao da biblioteca para ler o .env
from dotenv import load_dotenv
from os import getenv
# Criacao da engine para conexao com o BD
from sqlalchemy import create_engine
# Criacao da biblioteca para abertura da sessao
from sqlalchemy.orm import sessionmaker as sm


class DBConnection:
    '''Classe para controle de conexoes com multi BD's'''
    def __init__(self) -> None:
        # Carrega a funcao para ler param do .env
        # Como o construtor sempre será acionado quando
        # for instanciado, eu faco o atributo disparar a 
        # construcao da str de conexao
        self.__loader = self.load_init()
        # Guardo a str de conexao em um outro atributo, caso 
        # eu queira trocar de BD
        self.__string_mssql = self.__loader
        # Aciono atreves do atributo uma nova funcao para construcao
        # da engine
        self.__engine = self.__create_database_engine()
        # A sessao fica como none até que esta classe seja
        # instanciada, ai ele inicia automaticamente o metodo
        # magico chamado  "def __enter__(self):"
        self.session = None

    def load_init(self) -> None:
        '''Carregamento dos dados do .env que possui
        os dados de conexão para a string do BD'''
        # Acionamento do dotenv
        load_dotenv()
        # Dados para conexao provenientes do .env
        self.user = getenv('user')
        self.pw = getenv('pw')
        self.server = getenv('server')
        self.db = getenv('db')
        self.driver = getenv('driver')
        self.port = getenv('port')

        # Conexao com usuario e senha no sql, criacao da string de conexao com MSSQL
        str_db = f'mssql+pyodbc://{self.user}:{self.pw}@{self.server}/{self.db}?driver={self.driver}'
        # Devolve para o atributo a string montada
        return str_db

    def __create_database_engine(self):
        '''Controi uma engine sempre que a classe é instanciada.'''
        # Montagem da engine de conexao sob a str de conexao com o BD
        engine = create_engine(self.__string_mssql)
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
