# https://www.youtube.com/watch?v=RoYuIKkGUy8&list=PLYfSsxE6TZLsbszd4qVW114Aftn4aALAa&index=2

# Atr de class

class Pais:
    # Atr de class, disponível apenas para class
    pop_limite = 200
    # E possivel criar variaveis na class que recebe os paises que sao criados
    list_pais = []

    # Preciso chamar um metodo construtor
    def __init__(self, nome, cap, pop) -> None:
        self.nome = nome
        self.cap = cap
        self.pop = pop
        # Reutilizacao de dados do atr do obj
        self.abrv = str(self.nome[:2]).upper()
        # Sempre que meu contrutor chamar um novo obj, ele insere na list_pais
        # para isto preciso chamar a class e seu atributo
        Pais.list_pais.append(self)

    # Esta e um metodo magico dentro do meu construtor que entrega a
    # representacao
    # dos atributos do meu obj, com isto ele muda totalmente o meu resultado na
    # LINHA 49, comentar este metodo para ver o como ele sai la embaixo
    def __repr__(self) -> str:
        return self.nome


p1 = Pais('Brasil', 'Brasilia', 150)
p2 = Pais('Argentina', 'Buenos Aires', 50)

print(f'\nO {p1.nome} possui {p1.pop}M e uma capital chamada '
      f'{p1.cap} - {p1.abrv}')
print(f'\nO {p2.nome} possui {p2.pop}M e uma capital chamada '
      f'{p2.cap} - {p2.abrv}')

# Acessar o atr da class podera ser feito sem instaciar a class

print(f'\nEste é atr da class Pais {Pais.pop_limite}')

# Ao acessar um atr do obj, se o py nao achar, ele ira procurar na class
# para entao invocar um erro se nao encontrar na class

print(f'\nEstou procurando o atr no obj sem ele existir e'
      f'retorno o atr do class = {p1.pop_limite}')

# Lista dos pais como obj sendo um endereco de memoria
print(f'\nPaises como OBJS:\n{Pais.list_pais}')
