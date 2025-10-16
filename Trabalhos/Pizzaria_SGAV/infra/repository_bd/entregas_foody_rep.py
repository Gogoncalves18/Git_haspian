'''Na pasta de repository é reservado os foco dos cmds sql
a partir daqui é importado o ambiente de conexao com o BD,
DBConnection que possui as str de conexao. Importo tambem
as tabelas que pretendo gerar as consultas'''
from infra.configs.connection_db import DBConnection
from infra.entities_bd.entregas import Entregas_FoodyD
# Importacao da biblioteca para tratar erros no sql alchemy
from sqlalchemy.orm.exc import NoResultFound
from dotenv import load_dotenv
from os import getenv
from sqlalchemy import func


class Entregas_FoodyD_Repository:
    '''Classe responsável em gerar os comandos SQL para
    acesso ao BD através da ORM SQLAlchemy'''
    load_dotenv()
    bd_foody = getenv('db_foody')

    def select(self) -> list:
        bd = self.bd_foody
        '''Retorno de uma lista de instancias dentro da tabela
        modo_venda do Banco de dados.'''
        # Com o DBConnection e o cmd with, eu consigo gerar um
        # tipo de instancia que me retorna a conexao do BD com
        # a sessão aberta até finalizar a execução do comando.
        # Com esta sessão, é possível buscar os cmds do Alchemy
        with DBConnection(bd) as db:
            # Da conexão eu chamo a sessão e depois os cmds
            # A importacao de filmes define o mapping de BD que
            # estou fazendo
            '''Tratamento de erro no alchemy'''
            try:
                data = db.session.query(Entregas_FoodyD).all()
                return data
            except NoResultFound:
                return None

    def select_ultima_dt(self) -> list:
        bd = self.bd_foody
        '''Retorno de uma lista de instancias dentro da tabela
        modo_venda do Banco de dados.'''
        # Com o DBConnection e o cmd with, eu consigo gerar um
        # tipo de instancia que me retorna a conexao do BD com
        # a sessão aberta até finalizar a execução do comando.
        # Com esta sessão, é possível buscar os cmds do Alchemy
        with DBConnection(bd) as db:
            # Da conexão eu chamo a sessão e depois os cmds
            # A importacao de filmes define o mapping de BD que
            # estou fazendo
            '''Tratamento de erro no alchemy'''
            query2 = db.session.query(func.max(Entregas_FoodyD.idlag))

            try:
                # Uso "scalar_subquery" sempre que ha uma suquery
                # E o ".one()" é pq ele retornará apenas um resultado
                # se nao tiver nada na tabela, ele volta None no obj da query
                data = db.session.query(Entregas_FoodyD.datapedido
                                        ).where(Entregas_FoodyD.idlag ==
                                                query2.scalar_subquery()).one()
                return data
            except Exception as e:
                print(f"Erro ao usar one(): {e}")
                return None

    def insert_corridas(self,
                        numentrega: int,
                        uidcliente: str,
                        datapedido: str,
                        horapedido: str,
                        horapedpronto: str,
                        horapedaceito: str,
                        horapedentregue: str,
                        tempototentrega: str,
                        txentrega: str,
                        txmotoboy: str,
                        motoboy: str,
                        nomecliente: str,
                        telefone: str,
                        rua: str,
                        numresid: str,
                        cidade: str,
                        coletalat: str,
                        coletalong: str,
                        lat: str,
                        long: str,
                        obsv: str,
                        iddelivery: str,
                        dist: str,
                        tempodist: str
                        ) -> list:
        '''
        Funcao para percorrer dados de pedidos que estao dentro de uma [].
        Ela procura 24 variaveis dentro dos dados que estao organizados na
        lista recebida.
        '''
        bd = self.bd_foody
        # Com o DBConnection e o cmd with, eu consigo gerar um
        # tipo de instancia que me retorna a conexao do BD com
        # a sessão aberta até finalizar a execução do comando.
        # Com esta sessão, é possível buscar os cmds do Alchemy
        with DBConnection(bd) as db:
            # Da conexão eu chamo a sessão e depois os cmds
            # A importacao de filmes define o mapping de BD que
            # estou fazendo
            try:
                data_insert = Entregas_FoodyD(numentrega=numentrega,
                                              uidcliente=uidcliente,
                                              datapedido=datapedido,
                                              horapedido=horapedido,
                                              horapedidopronto=horapedpronto,
                                              horapedidoaceito=horapedaceito,

                                              horapedidoentregue=horapedentregue,
                                              tempopedido=tempototentrega,
                                              txentrega=txentrega,
                                              txmotoboy=txmotoboy,
                                              motoboy=motoboy,
                                              nomecliente=nomecliente,
                                              telefone=telefone,
                                              rua=rua,
                                              numresd=numresid,
                                              cidade=cidade,
                                              latcoleta=coletalat,
                                              longcoleta=coletalong,
                                              lat=lat,
                                              long=long,
                                              obspedido=obsv,
                                              iddelivery=iddelivery,
                                              dist=dist,
                                              tempodist=tempodist
                                              )
                # Uso "scalar_subquery" sempre que ha uma suquery
                # E o ".one()" é pq ele retornará apenas um resultado
                # se nao tiver nada na tabela, ele volta None no obj da query
                db.session.add(data_insert)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
