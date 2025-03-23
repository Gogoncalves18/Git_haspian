import pyodbc
from dotenv import load_dotenv
from os import getenv


class ConectorBD:
    def __init__(self, driver, local_instancia_bd, nome_db,
                 username, pw, trust_conect):
        self.__driver = driver
        self.__local_inst = local_instancia_bd
        self.__nome_db = nome_db
        self.__user = username
        self.__pw = pw
        self.__trust = trust_conect
        # Instacio o metodo para ele executar a conexao em BD
        # ja na propria construcao do objeto
        self.conex = self.conectar_bd()

    def conectar_bd(self) -> None:
        '''
        Metodo para gerar a string de conexao e abrir a conexao com
        o BD. Ele printa a saida com sucesso ou falha nesse processo.
        '''
        self.str_conex = f"DRIVER={self.__driver}; SERVER={
                    self.__local_inst}; DATABASE={
                    self.__nome_db}; UID={self.__user}; PWD={
                    self.__pw}; TRUSTED_CONNECTION={self.__trust}"

        self.conexao_bd = pyodbc.connect(self.str_conex)
        if self.conexao_bd:
            print('>>> CONEXAO COM BD ESTABELECIADA')
            return self.conexao_bd
        else:
            print('!!!! FALHA NA CONEXAO COM O BD !!!!')

    def get_cur(self) -> object:
        '''
        Funcao para dar o objeto instanciado do PYODBC
        com a conexao aberta com o BD
        '''
        return self.conex


if __name__ == '__main__':

    load_dotenv()

    driver = getenv('driver')
    server = getenv('server')
    db_pdv = getenv('db_pdv')
    username = getenv('username')
    password = getenv('password')
    tc = getenv('tc')

    ex = ConectorBD(driver, server, db_pdv, username, password, tc)
    ex.conectar_bd()
