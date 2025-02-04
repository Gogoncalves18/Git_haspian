# No POO, proteger um atributo é o processo de encapsulamento,
# um dos pilares importantes do POO, para setarmos valores
# para os atributos, precisamos montar funcoes para isto Getter e Setter


class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf
        self.__time = None

    ''''Veja que por dentro da classe que eu permito a alteracao atraves
    de uma funcao. Reparar que "time: str" indica que esperamos uma string
    para que a funcao funcione e "-> None" indica que ela nao retornara
    nada'''
    def setter_time(self, time: str) -> None:
        self.__time = time

    def getter_time(self) -> str:
        return self.__time

    '''É possivel usar o "@property" para chamar o atribudo, neste caso
    eu não uso o () na chamado do metodo, eu chamo desta forma:
    "gus.getter_time"'''
    @property
    def getter_time(self) -> str:
        return self.__time

    def apresentar(self):
        print(f'REF001 - Ola! Minha altura é {self.altura}.')
        self.__coletar_doc()

    def __coletar_doc(self):
        print(f'\t E meu cpf é {self.__cpf}.')
        # print(f'\t E meu cpf é {self.cpf}.')


gus = Pessoa(1.80, cpf='345.832.444-00')
ze = Pessoa(1.60, cpf='324.000.002-10')

# Forma de definir um atributo para um objeto
gus.setter_time('Gremio')

gus.apresentar()
#print(f'O time de dele é o {gus.getter_time()}.\n')
print(f'O time de dele é o {gus.getter_time}.\n')

ze.apresentar()
#print(f'O time de dele é o {ze.getter_time()}')
