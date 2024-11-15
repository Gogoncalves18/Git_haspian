class Loja:
    tx = 1.1

    def __init__(self, prod, vlr_bruto: float) -> None:
        self.prod = prod
        self.vlr_bruto = vlr_bruto

    def consult_vlr(self) -> None:
        print(f'O item {self.prod} custa R${self.vlr_bruto * self.tx}')

    @classmethod
    def editar_tx(cls, vlr_tx: float) -> None:
        cls.tx = vlr_tx

    def __repr__(self) -> str:
        return self.prod


# Exemplo de como podemos fazer uma variavel de classe afetar todos os objetos
camisa = Loja('Camisa', 50)
calca = Loja('Calca', 100)
camisa.consult_vlr()
calca.consult_vlr()
Loja.editar_tx(2)
print('\nDobrei a taxa\n')
camisa.consult_vlr()
calca.consult_vlr()
