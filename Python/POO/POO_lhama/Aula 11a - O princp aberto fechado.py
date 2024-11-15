class Artista:
    def __init__(self, art: str) -> None:
        self.art = art

    def apresentar_show(self) -> None:
        print(f'\nO artista {self.art} esta apresentando o show\n')


class Circo:
    def apresentar(self, artista: Artista) -> None:
        print('\nO circo abre o esperátaculo.')
        artista.apresentar_show()
        print('O esperátaculo terminou.')


circo = Circo()
# Desta forma é possível criar vários personagem sem ficar
# alterando o código fonte, estou extendendo o recurso
# sem altera-lo. Tenho uma relação de "Associação"

palhaco = Artista('Palhaço')
domador = Artista('Domador de Leões')
mulher_elastico = Artista('Mulher elástico')
motoqueiro = Artista('Motoqueiro Fantasma')

circo.apresentar(palhaco)
circo.apresentar(domador)
circo.apresentar(mulher_elastico)
circo.apresentar(motoqueiro)
