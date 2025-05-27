# Importacao para fazer o mapping da tabela
from infra.configs.base import Base_decl
# Importacao da tipagem para declarar a tabela do SQL
from sqlalchemy import Column, String, Integer
# Importacao da relacao reversa dentro de uma tabela para outra
from sqlalchemy.orm import relationship


class Filmes(Base_decl):
    # Cmd para identificar para o alchemy que este mapping é da
    # tabela filmes do BD
    __tablename__ = "filmes"

    # Especificacao das colunas
    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    # aqui entro com um relação reversa, ela se chama assim
    # pq a relacao é da tabela de atores com o id titulo do filme
    # la em atores que eu aponto para uma foreingkey, porem aqui 
    # conseguiremos chegar em atores pela tabela principal
    artistas = relationship('Atores', backref='atores', lazy='subquery')

    # Definicao de uma funcao para printar dados da tabela
    def __repr__(self):
        return f'Filme => (Titulo= {self.titulo} -- Ano= {self.ano})'
