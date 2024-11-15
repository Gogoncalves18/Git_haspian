class Mamifero:
    def __init__(self, local: str) -> None:
        # Atr publico
        self.localicazacao = local

    def andar(self) -> None:
        print(f'\nO animal está andando pelo {self.localicazacao}')

    def _dormir(self) -> None:
        print('O animal está dormindo')


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
        # Este seria um metodo protegido como indicacao, mas não
        # é bloqueado pelo py, esta é uma convenção.
        self._dormir()


fred = Gato('COLOMBIA')
fred.miar()
