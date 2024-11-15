'''O S do SOLID diz que parte do meu programa devem ter uma unica funcao,
veja o caso abaixo, ele não possui uma única funcao:

def cadastrar(self, nome: str, idade: int) -> None:
        # Validacao se o obj recebido é uma str e um inteiro
        if isinstance(nome, str) and isinstance(idade, int): # Aqui eu firo o "S" porque estou validando
            print('Acessando o BD...') # Acessando o BD é uma segunda funcao
            print(f'Cadastrando o nome {nome} e a idade de {idade} anos.') # Cadastrando é uma terceira funcao
        else:
            print('Dados inválidos!')

Assim reescrevemos da seguinte forma'''


class SistemaCadastro:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validate_input(nome, idade):  # Passei a validacao para um metodo
            self.__valida_conex()  # Acessando o BD passei para um metodo
            self.__cadastra_dados(nome, idade)  # Cadastro no BD foi isolado em uma funcao
        else:
            self.__err()

    # Este é o principio da responsabilidade unica, separando cada modulo em uma funcao
    # unica e isolada
    def __validate_input(self, nome: str, idade: int) -> bool:
        # Meu retorno já é a validacao sendo realizada
        return isinstance(nome, str) and isinstance(idade, int)

    def __valida_conex(self) -> None:
        print('Acessando o BD...')

    def __cadastra_dados(self, nome: str, idade: int) -> None:
        print(f'Cadastrando o nome {nome} e a idade de {idade} anos.')

    def __err(self) -> None:
        print('Dados inválidos!')


p1 = SistemaCadastro()
p1.cadastrar('Gustavo', 42)

# Parei em 7min
