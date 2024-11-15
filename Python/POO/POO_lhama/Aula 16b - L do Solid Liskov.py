class ConnctionDB:
    def conectar(self):
        print('\nConectando ao BD')


class SQLRepository(ConnctionDB):
    def select(self):
        print('Buscando dados no BD SQL')


class MariaDB(ConnctionDB):
    def select(self):
        print('Buscando dados no BD MARIA')


class DBHandler():
    def alter_table(self):
        print('Alterando tabela em SQL')

'''Veja que herdamos na classe de conexao ao BD apenas as classes pai
que de alguma forma podem serem trocadas pela classe filha. Ja o 
DBHandler() possui um aler_table() que não contlempla o mesmo altertable
dao MARIA DB, portanto eu não posso herdar de SQLRepository ou MariaDB,
caso contrário quebraria o principio de Liskov'''
