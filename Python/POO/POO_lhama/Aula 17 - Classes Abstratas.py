from abc import ABC, abstractmethod


# Em py isto seria uma interface, uma definicao de como devemos
# implementar a classe
class Trabalhador(ABC):

    @abstractmethod
    def trabalhar(self) -> None: ...

    @abstractmethod
    def ir_para_casa(self) -> None: ...

    @abstractmethod
    def horario_almoco(self) -> None: ...


class Professor(Trabalhador):
    def trabalhar(self) -> None:
        print('O Professor esta trabalhando')

    def ir_para_casa(self) -> None:
        print('O professor está indo para casa')

    def horario_almoco(self) -> None:
        print('O professor está almoçando')


class Engenheiro(Trabalhador):
    def trabalhar(self) -> None:
        print('O Engenheiro esta trabalhando')

    def ir_para_casa(self) -> None:
        print('O Engenheiro está indo para casa')

    def horario_almoco(self) -> None:
        print('O Engenheiro está almoçando')


# Neste caso estou tipando a entrada da função com uma interface,
# que obrigará a implementar os métodos necessários para o código
# funcionar
def comunicar_trabalhador(profissional: Trabalhador):
    profissional.trabalhar()
    print('Comunicar o trabalhador para ir para casa')
    profissional.ir_para_casa()


p1 = Professor()
p2 = Engenheiro()

print()
comunicar_trabalhador(p1)
print('#####################')
comunicar_trabalhador(p2)
print()
