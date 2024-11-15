class Produto:
    def __init__(self, nome: str, valor: int) -> None:
        self.__nome = nome
        self.__valor = valor

    def infos_produto(self) -> None:
        print(f'\n>>>>Produto: {self.__nome} - Valor: {self.__valor} <<<<')


class CarrinhoCompras:
    def __init__(self) -> None:
        self.__produtos_carrinho = []

    # Processo de agregacao, onde instancio objetos dentro da classe
    # e compartilho ela para outra classe
    def adicionar_produtos(self, produto_desejado: Produto) -> None:
        self.__produtos_carrinho.append(produto_desejado)

    def finalizar_compra(self) -> None:
        print('\nCompra finalizada!')
        print("     >>>> Meus Produtos:     <<<<")
        for p in self.__produtos_carrinho:
            p.infos_produto()


p1 = Produto('Camisa', 54.90)
p2 = Produto('Calça', 129.30)
p3 = Produto('cueca', 10.15)

carrinho = CarrinhoCompras()
carrinho.adicionar_produtos(p1)
carrinho.adicionar_produtos(p2)
carrinho.adicionar_produtos(p3)

carrinho.finalizar_compra()
