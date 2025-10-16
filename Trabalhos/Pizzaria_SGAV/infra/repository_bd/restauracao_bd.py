import pyodbc
from dotenv import load_dotenv
from os import getenv


class Restauracao_BD:
    ''' Função de SQL puro para restauração de Banco de Dados'''

    def __init__(self):
        self.__loader = self.__load()

    def __load(self):
        load_dotenv()
        self.user = getenv('userdb')
        self.pw = getenv('password')
        self.server = getenv('server')
        self.db = getenv('db_pdv')
        self.driver = getenv('driver')
        self.port = getenv('port')
        self.tc = 'yes'
        self.bak = getenv('local_bak')
        self.str_db = f"DRIVER={self.driver}; SERVER={self.server}; DATABASE={
                        self.db}; UID={self.user}; PWD={
                        self.pw}; TRUSTED_CONNECTION={self.tc}"

        return self.str_db

    def restaurar_sql(self):

        '''Funcao para restauracao de backup de DB. A funcao deve receber
        o caminho completo e o nome do arquivo.bak'''

        # Abre conexao com o BD
        conex = pyodbc.connect(self.__loader)
        # Parametro executar obrigatoriamente commit no BD
        # (consolidacao do dados)
        conex.autocommit = True
        # instacia o cursor do sql
        cursor_sql = conex.cursor()
        # estrutura do script do sql, primeiro uso o master para nao estar
        # concorrendo com o uso do BD enquanto tiver escrevendo o bckup.
        # depois aponto o nome do BD 'ncrcolibri' o local onde esta o bak e
        # a instrucao with replace para apenas substituir o bd ao inves
        # de regravar

        cmd1 = f"""USE MASTER; RESTORE DATABASE PDV FROM DISK='{
            self.bak}' WITH REPLACE;"""

        try:
            # executa o cmd
            cursor_sql.execute(cmd1)
            # aqui um segredo, enquanto ocorre a restauracao do BD,
            # o cursor fica em aberto, se ele ler a linha abaixo que define
            # o fechamento da conexao, a restauracao do bak nao ocorre.
            # neste caso o sistema fica em loop validando se o cursor ainda
            # esta em aberto com o cursor_sql.nextset(), apos uma negativa
            # eu saiu do laco e entao encerro a conexao
            while cursor_sql.nextset():
                pass
            cursor_sql.close()
            print('>>> RESTAURAÇÃO DE BD BEM SUCEDIDA! <<<')
        except pyodbc.DatabaseError as avisos:
            print(f'>>> PROBLEMA COM A MANIPULAÇÃO DO SQL\n:{avisos}')
            conex.rollback()
        finally:
            # linha de seguranca para o caso de dar tudo certo
            conex.close()
