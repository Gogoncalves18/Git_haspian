# Importacao para fazer o mapping da tabela
from infra.configs.base import base_decl
# Importacao da tipagem para declarar a tabela do SQL
from sqlalchemy import Column, String, Integer, TIME, DATE, FLOAT


class Entregas_FoodyD(base_decl):
    # Cmd para identificar para o alchemy que este mapping é da
    # tabela do BD
    __tablename__ = "entregas"

    # Especificacao das colunas
    idlag = Column(Integer, primary_key=True)
    numentrega = Column(Integer, nullable=False)
    uidcliente = Column(String, nullable=False)
    datapedido = Column(DATE, nullable=False)
    horapedido = Column(TIME, nullable=False)
    horapedidopronto = Column(TIME, nullable=False)
    horapedidoaceito = Column(TIME, nullable=False)

    horapedidoentregue = Column(TIME, nullable=True)
    tempopedido = Column(TIME, nullable=True)
    txentrega = Column(FLOAT, nullable=True)
    txmotoboy = Column(FLOAT, nullable=True)
    motoboy = Column(String, nullable=True)
    nomecliente = Column(String, nullable=True)
    telefone = Column(String, nullable=True)
    rua = Column(String, nullable=True)
    numresd = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    lat = Column(String, nullable=False)
    long = Column(String, nullable=False)
    latcoleta = Column(String, nullable=False)
    longcoleta = Column(String, nullable=False)
    obspedido = Column(String, nullable=True)
    iddelivery = Column(String, nullable=True)
    dist = Column(String, nullable=True)
    tempodist = Column(String, nullable=True)

    def __repr__(self):
        return f'{self.idlag} {self.uidcliente}'
