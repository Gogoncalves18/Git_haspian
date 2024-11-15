from .Interfaces.elemento_interface import ElementoInterface


class Elemento(ElementoInterface):
    def executar(self) -> None:
        print('\nEstou executando do ELEMENTO\n')
