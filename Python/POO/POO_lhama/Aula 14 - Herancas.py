class Mamifero:
    def __init__(self, local: str) -> None:
        # Atr publico
        self.localicazacao = local

    def andar(self) -> None:
        print(f'\nO animal está andando pelo {self.localicazacao}')


# Forma que herdamos os atr e metodos de uma classe superior
class Cachorro(Mamifero):
    def __init__(self, local: str) -> None:
        super().__init__(local)
        self.tipo = 'Dog'

    def latir(self) -> None:
        # Neste caso não preciso passar a localizacao para o classe
        # porque ela é de acesso publico na classe superior
        print(f'\nO {self.tipo} está andando e latindo pelo '
              f'{self.localicazacao}')
        self.andar()


class Gato(Mamifero):
    def __init__(self, local: str) -> None:
        super().__init__(local)
        self.tipo = 'Gato'

    def miar(self) -> None:
        # Neste caso não preciso passar a localizacao para o classe
        # porque ela é de acesso publico na classe superior
        print(f'\nO {self.tipo} está andando e miando pelo '
              f'{self.localicazacao}')
        self.andar()


animal = Mamifero('BRASIL')
animal.andar()

raj = Cachorro('ARGENTINA')
raj.latir()

fred = Gato('COLOMBIA')
fred.miar()
