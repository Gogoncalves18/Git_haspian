# https://www.youtube.com/watch?v=RoYuIKkGUy8&list=PLYfSsxE6TZLsbszd4qVW114Aftn4aALAa&index=1

# Nome da class sempre com a primeira letra em maiusculo
class Pais:
    pass


p1 = Pais()

# Ver o tipo do obj, é um obj do tipo pais
print(type(p1))

# Forma de colocar um atributo no obj, seu atributos continuam 
# do mesmo tipo porem pertecente a uma class, porem esta estrutura
# nao e ideal

p1.name = 'Brasil'
p1.capital = 'Brasilia'
p1.populacao = 212.6

print(f'\nO {p1.name} possui {p1.populacao}M e uma capital chamada '
      f'{p1.capital}')

# Estrutura de uma class


class Pais2:
    # Preciso chamar um metodo construtor
    def __init__(self, nome, cap, pop) -> None:
        self.nome = nome
        self.cap = cap
        self.pop = pop
        # Reutilizacao de dados do atr do obj
        self.abrv = str(self.nome[:2]).upper()


p2 = Pais2('Argentina', 'Buenos Aires', 105)
print(f'\nO {p2.nome} possui {p2.pop}M e uma capital chamada '
      f'{p2.cap} - {p2.abrv}')
