from modulos.conexao_bds import ConectorBD


class RepositorioBD:
    '''
    Classe que contem os metodos para CRUD do BD.
    '''

    def __init__(self, connector: ConectorBD):
        # Injecao de dependencia da Classe Repositorio por um OBJ
        # que faca a conexao com o BD
        self.conn = connector

    def consulta_ped(self) -> list:
        # Com o obj do pyodbc, chamo um metodo que me retorna o obj
        # para apartir dele executar as acoes. Neste caso pego o cursor
        cursor = self.conn.get_cur()
        cur = cursor.cursor()
        # CMD SQL
        cmd_cons = "select vl_subtotal_itens from dbo.operacao_venda_geral"

        try:
            dados = cur.execute(cmd_cons).fetchall()
        except Exception as err:
            print(f"Aviso: {err}")
            cursor.rollback()
        finally:
            cursor.close()
        return dados
    
    def restaurar_bck(self, nome_bd, bak):
        '''
        Funcao para restauracao de backup de DB. A funcao deve receber
        o caminho completo e o nome do arquivo.bak
        '''

        # Abre conexao com o BD
        cursor = self.conn.get_cur()
        cur = cursor.cursor()
        # Parametro executar obrigatoriamente commit
        # no BD (consolidacao do dados)
        
        # cursor.autocomit = True
        cursor.autocomit = True
        # instacia o cursor do sql
        
        # estrutura do script do sql, primeiro uso o master para nao estar
        # concorrendo com o uso do BD enquanto tiver escrevendo o bckup.
        # depois aponto o nome do BD 'ncrcolibri' o local onde esta o bak e
        # a instrucao with replace para apenas substituir o bd ao inves
        # de regravar
        cmd1 = f"""USE MASTER; RESTORE DATABASE PDV FROM DISK='{bak}' WITH REPLACE;"""
        try:
            # executa o cmd
            cur.execute(cmd1)
            # aqui um segredo, enquanto ocorre a restauracao do BD,
            # o cursor fica em aberto, se ele ler a linha abaixo que define
            # o fechamento da conexao, a restauracao do bak nao ocorre.
            # neste caso o sistema fica em loop validando se o cursor ainda
            # esta em aberto com o cursor_sql.nextset(), apos uma negativa
            # eu saiu do laco e entao encerro a conexao
            while cur.nextset():
                pass
            cur.close()
        except Exception as err:
            print(f'PROBLEMA COM A MANIPULAÇÃO DO SQL\n:{err}')
            cursor.rollback()
        finally:
            # linha de seguranca para o caso de dar tudo certo
            cursor.close()
            

