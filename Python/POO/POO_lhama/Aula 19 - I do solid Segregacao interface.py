from abc import ABC, abstractmethod


# Em py isto seria uma interface, uma definicao de como devemos
# implementar a classe
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None: ...

    @abstractmethod
    def ir_para_casa(self) -> None: ...

    @abstractmethod
    def consultar_beneficios(self) -> None: ...


class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print('O Professor esta trabalhando')

    def ir_para_casa(self) -> None:
        print('O professor está indo para casa')

    def consultar_beneficios(self) -> None:
        print('Consultando beneficios')


class ProfessorSubstitudo(Trabalhador):
    def trabalhar(self) -> None:
        print('O Professor esta trabalhando')

    def ir_para_casa(self) -> None:
        print('O professor está indo para casa')

    # Nesta classe estou quebrando o princípio da segregração de interface
    def consultar_beneficios(self) -> None:
        pass


p2 = ProfessorSubstitudo()
