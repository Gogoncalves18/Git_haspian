# Importacao para fazer o mapping da tabela
from infra.configs.base import base_decl
# Importacao da tipagem para declarar a tabela do SQL
from sqlalchemy import Column, String, Integer


class Modo_Venda(base_decl):
    # Cmd para identificar para o alchemy que este mapping é da
    # tabela do BD
    __tablename__ = "modo_venda"

    # Especificacao das colunas
    id = Column(Integer, primary_key=True)
    codigo = Column(Integer, nullable=False)
    nome = Column(String, nullable=False)

    # Definicao de uma funcao para printar dados da tabela
    def __repr__(self):
        return f'Tipos de Venda => (ID= {self.id} -- Tipo= {self.nome} -- COD= {self.codigo})'
