class Circo:
    def apresentar(self, cmd: int) -> None:
        if cmd == 1:
            self.__show_palhaco()
        if cmd == 2:
            self.__show_malabarista()

    def __show_palhaco(self):
        print('\nO Palhaco esta apresentando o show\n')
    
    def __show_malabarista(self):
        print('\nO Malabarista esta apresentando o show\n')


'''O problema deste codigo é que se houver um novo artista para se apresentar,
nós precisamos inevitavelmente alterar o a primeira funcao da classe e também
criar uma def nova. Isto fere o princípio do aberto/fechado, veja na Aula 11a
a alternativa para atender o princípio.
'''
circo = Circo()
cmd = 2
circo.apresentar(cmd)
