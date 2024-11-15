class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.comodo = comodo

    def acender(self) -> None:
        print(f'Ligou a luz do comodo {self.comodo}')

    def apagar(self) -> None:
        print(f'Apagou a luz do comodo {self.comodo}')


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

    '''Este é o tipo de associação entre classes, a "tomada" é tipada
    como uma classe, com isto eu consigo usar os metodos dela. Mas se eu perder
    a tomada, a minha classe nao para de funcionar'''
    def acender_luzes(self, tomada: Interruptor):
        print(f'O {self.nome}')
        tomada.acender()

    def apagar_luzes(self, tomada: Interruptor):
        print(f'O {self.nome}') 
        tomada.apagar()


gu = Pessoa('Gustavo')
luz_sala = Interruptor('Sala')
luz_coz = Interruptor('Cozinha')
luz_garagem = Interruptor('Garagem')

'''Aqui podemos ver que a classe pessoa usa um metodo que recebe
um objeto que foi instaciado em outra classe'''
gu.acender_luzes(luz_sala)
gu.acender_luzes(luz_coz)
gu.acender_luzes(luz_garagem)
gu.apagar_luzes(luz_sala)
gu.apagar_luzes(luz_coz)
gu.apagar_luzes(luz_garagem)