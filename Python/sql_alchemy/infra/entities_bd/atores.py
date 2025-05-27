# Importacao para fazer o mapping da tabela
from infra.configs.base import Base_decl
# Importacao da tipagem para declarar a tabela do SQL
from sqlalchemy import Column, String, Integer, ForeignKey


class Atores(Base_decl):
    # Cmd para identificar para o alchemy que este mapping é da
    # tabela filmes do BD
    __tablename__ = "atores"

    # Especificacao das colunas
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    # Maneira de transformar o id de uma tabela conectado com o id de outra
    titulo_filme = Column(String, ForeignKey("filmes.titulo"))

    # Definicao de uma funcao para printar dados da tabela
    def __repr__(self):
        return f'Ator => {self.nome} fez o filme {self.titulo_filme}'
