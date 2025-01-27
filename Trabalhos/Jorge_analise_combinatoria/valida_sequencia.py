# Validacao do jogo - Procura se ha sequencias dentro da jogada
# combinada. Info e cada numero dentro da jogada


def validar_sequencia(jogo_valido_par_impar: tuple, qtd_de_seq: int, possib: int):
    # Variavel de comparacao para controle da sequencia
    v = None
    v2 = None
    # Quantidade de sequencias existentes no jogo
    qtd_rep = 0
    # Definicao se ha ou nao sequencia
    possui_seq = False
    for info in jogo_valido_par_impar:
        # Contador da variavel comeca vazio no primeiro numero
        if v is None:
            v = info
        else:
            v = info
        if v == v2:
            v2 = v + 1
            qtd_rep += 1

            # Valor para 1 sequencia ou 2 numeros em sequencia
            if qtd_rep >= qtd_de_seq:
                possui_seq = True
        else:
            # print('OK')
            v2 = v + 1
            if possui_seq is False:

                # Valor para 1 sequencia ou 2 numeros em sequencia
                if qtd_rep >= qtd_de_seq:
                    possui_seq = True
                qtd_rep = 0
    if possui_seq is True:
        print(f'JOGO {possib} com 4 SEQUENCIA => {jogo_valido_par_impar}')
        return 0
    else:
        return jogo_valido_par_impar