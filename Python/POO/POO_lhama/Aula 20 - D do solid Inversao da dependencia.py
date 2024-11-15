from Aula_20.Interfaces.elemento_interface import ElementoInterface
from Aula_20.elemento import Elemento
from Aula_20.elemento_OUTRO import Elemento_Outro


class Principal:
    '''Para evitar uma ligação forte entre a class principal e a classe
    elemento, associamos ela a Interface "ElementoInterface"'''
    def __init__(self, elem: ElementoInterface) -> None:
        self.__elem = elem

    def run(self) -> None:
        self.__elem.executar()
        print('Estou executando da classe PRINCIPAL')


# Instacio em um obj a classe elemento no programa, sem estar dentro
# da classe, assim tirando a relação direta.
el = Elemento()
el2 = Elemento_Outro()

# Injeto o obj na outra classe que esta aguardando um obj
# caracterizado por uma interface. Neste caso posso trocar a minha class
# inteira por "el" ou "el2" que minha class principal continua funcionando
cl1 = Principal(el2)
cl1.run()
