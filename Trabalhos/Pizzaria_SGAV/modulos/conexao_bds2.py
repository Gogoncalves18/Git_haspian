import pyodbc
from dotenv import load_dotenv
from os import getenv


class ConectorBD:
    def __init__(self, driver, local_instancia_bd, nome_db,
                 username, pw, trust_conect):
        self.driver = driver
        self.local_inst = local_instancia_bd
        self.nome_db = nome_db
        self.user = username
        self.pw = pw
        self.trust = trust_conect
        # Instacio o metodo para ele executar a conexao em BD
        # ja na propria construcao do objeto
        self.bd_ativo = self.conectar_bd()

    def conectar_bd(self) -> None:
        '''
        Metodo para gerar a string de conexao e abrir a conexao com
        o BD. Ele printa a saida com sucesso ou falha nesse processo.
        '''
        self.str_conex = f"DRIVER={self.driver}; SERVER={
                    self.local_inst}; DATABASE={
                    self.nome_db}; UID={self.user}; PWD={
                    self.pw}; TRUSTED_CONNECTION={self.trust}"

        self.conexao_bd = pyodbc.connect(self.str_conex)
        self.cnx = self.conexao_bd
        
        if self.cnx:
            print('>>> CONEXAO COM BD ESTABELECIADA')
            return self.cnx
        else:
            print('!!!! FALHA NA CONEXAO COM O BD !!!!')
    @classmethod
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
    pont = ex.get_cur
    

    
