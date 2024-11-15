class QualquerCoisa:
    def fazer(self) -> None:
        print('\nEstou fazendo algo.')


class OutraCoisa(QualquerCoisa):
    def preparar(self) -> None:
        print('Estou preparando algo')

    # No caso do polimorfismo, uma estratégia é usar a mesma assinatura de
    # métodos para classes diferentes porém com lógicas de construção
    # diferentes

    def fazer(self) -> None:
        print('\nEstou fazendo OUTRA COISA da classe outra coisa.')


obj1 = QualquerCoisa()
obj2 = OutraCoisa()

obj1.fazer()
obj2.fazer()
obj2.preparar()
