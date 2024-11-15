class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f'REF001 - Ola! Minha altura é {self.altura}.')
        self.__coletar_doc()

    def __coletar_doc(self):
        print(f'\t E meu cpf é {self.__cpf}.')
        # print(f'\t E meu cpf é {self.cpf}.')


gus = Pessoa(1.80, cpf='345.832.444-00')
ze = Pessoa(1.60, cpf='324.000.002-10')

''' O metodo com dois underline é um metodo privado, portanto ele poderá ser
# acessado somente pela classe. Isto também funciona para atributo'''
# gus.__coletar_doc()
'''No caso abaixo podemos ver que eu estou criando um atr e nao mais editando
meu atr'''
gus.cpf = 'xxxxxx'


gus.apresentar()


