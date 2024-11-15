class Torcedor_Estado:
    time = 'Gremio'

    def __init__(self) -> None:
        pass

    def troca_time(self, novo_time: str) -> None:
        self.time = novo_time

    def mostrar_time(self) -> None:
        print(f'Time dele é {self.time}')


p1 = Torcedor_Estado()
p2 = Torcedor_Estado()

'''Isto mostra que uma variavel estatica de classe pode ser alterado
de fora, mas ela não assumirá a alteração em todos os objetos quando
executado o cmd da linha REF001, pois esta variavel está somente 
definida no escopo da classe, já no contexto do obj nós definimos 
um time  no REF002, este sim não sofrerá com a alteracao'''
p1.mostrar_time()
p2.troca_time('Inter')  # REF002
p2.mostrar_time()
print(Torcedor_Estado.time)
Torcedor_Estado.time = 'Caxias'  # REF001
p1.mostrar_time()
p2.mostrar_time()


class Torcedor_nacional:
    time = 'BRASIL'

    def __init__(self) -> None:
        pass

    @classmethod
    def troca_time(cls, novo_time: str) -> None:
        cls.time = novo_time

    def mostrar_time(self) -> None:
        print(f'Time dele é {self.time}')


print('\n#######################################')
p1 = Torcedor_nacional()
p2 = Torcedor_nacional()

'''Agora podemos ver que o "classmethod" acionado na linha
REF003 fez com que todos os obj criados, mesmo que tenha sido
com outro valor, foram novamente alterados para Colombia,
como é o caso do p1 que primeiro era Brasil e depois aparecei como
Colombia sem ter sido solicitado para alteração'''
p1.mostrar_time()
p2.troca_time('Colombia')  # REF003
p2.mostrar_time()
print(Torcedor_Estado.time)
p1.mostrar_time()
p2.mostrar_time()
