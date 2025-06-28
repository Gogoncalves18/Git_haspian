'''Na pasta de repository é reservado os foco dos cmds sql
a partir daqui é importado o ambiente de conexao com o BD,
DBConnection que possui as str de conexao. Importo tambem
as tabelas que pretendo gerar as consultas'''
from sqlalchemy import text
from infra.configs.connection_db import DBConnection
# Importacao da biblioteca para tratar erros no sql alchemy
# from sqlalchemy.orm.exc import NoResultFound


class Restaurar_BD:
    '''Classe responsável em gerar os comandos SQL para
    acesso ao BD através da ORM SQLAlchemy'''

    def restaurar_sql(self):
        '''
        Funcao para restauracao de backup de DB. A funcao deve receber
        o caminho completo e o nome do arquivo.bak
        '''

        # estrutura do script do sql, primeiro uso o master para nao estar
        # concorrendo com o uso do BD enquanto tiver escrevendo o bckup.
        # depois aponto o nome do BD 'ncrcolibri' o local onde esta o bak e
        # a instrucao with replace para apenas substituir o bd ao inves de regravar
        # cmd1 = f"USE MASTER; RESTORE DATABASE PDV FROM DISK='{bak}' WITH REPLACE;"
        bak = 'C:\\Program Files\\Microsoft SQL Server\\MSSQL16.SGAG\\MSSQL\\Backup\\ncrcolibri.bak'
        cmd = f"""USE MASTER; RESTORE DATABASE NCRCOLIBRI FROM DISK = '{bak}' WITH REPLACE;"""
        restore_sql = text(cmd)

        # Abre conexao com o BD
        with DBConnection() as db:
            try:
                db.session.execute(restore_sql)
                db.session.commit()
                print("Restauração concluída com sucesso!")
            except Exception as err:
                print(f'PROBLEMA COM A MANIPULAÇÃO DO SQL\n:{err}')
                db.session.rollback()
                db.session.close()
