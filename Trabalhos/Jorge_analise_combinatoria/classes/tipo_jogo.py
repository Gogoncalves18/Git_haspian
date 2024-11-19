class Jogo:
    '''Necessário receber como param:
    'qtd_campos' -> número de campos para montar o jogo.
    'tipo_jogo' -> definição do tipo de jogo, 2 (Dupla) ou 3 (Trio)
    ou 4 (Quadra).

    '''

    def __init__(self, qtd_campos: int, tipo_jogo: int) -> None:
        self.__qdt_campos = qtd_campos
        self.__tipo_jogo = tipo_jogo
        self.__jogo = self.__definir_jogo()
        self.__vlrs_campo = []
        self.__vlrs_para_campos = {}

    def __definir_jogo(self) -> str:
        if self.__tipo_jogo == 2:
            return 'Dupla'
        elif self.__tipo_jogo == 3:
            return 'Trio'
        elif self.__tipo_jogo == 4:
            return 'Quadra'
        else:
            raise Exception('\n\tERRO: Você não digitou um tipo de jogo \
                            válido!\n')

    def definir_vlrs_campos(self) -> None:
        for campo in self.__qdt_campos:
            for pos in range(0, self.__tipo_jogo):
                vlr_campo = int(input(f'>>>>> DEFINA PARA {self.__jogo}, '
                                      f'o {pos+1}º VALOR (de 1 à 100) PARA '
                                      f'O CAMPO {campo}: '))
                self.__vlrs_campo.append(vlr_campo)
            self.__vlrs_para_campos[campo] = self.__vlrs_campo
            self.__vlrs_campo = []
        return self.__vlrs_para_campos, self.__jogo
