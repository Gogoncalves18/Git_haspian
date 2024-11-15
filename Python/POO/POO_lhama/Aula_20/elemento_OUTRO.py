from .Interfaces.elemento_interface import ElementoInterface


class Elemento_Outro(ElementoInterface):
    def executar(self) -> None:
        print('\nEstou executando de  uma OUTRO ELEMENTO ALTERNATIVO\n')
