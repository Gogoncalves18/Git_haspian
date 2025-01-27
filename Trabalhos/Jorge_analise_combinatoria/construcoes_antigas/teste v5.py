linJ = {1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        2: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        3: [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        4: [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        5: [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
        6: [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
        7: [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
        8: [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
        9: [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
        10: [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]}

# Resultados gerados
j1 = [6, 17, 28, 39, 50, 60]  # invalido (diagonal 5x)
j2 = [28, 39, 50, 61, 72, 83]  # valido
j3 = [2, 13, 24, 35, 57, 68]  # valido (com um pulo)
j4 = [1, 12, 23, 34, 56, 67, 78, 89, 100]  # invalido (diagonal 5x)
j5 = [1, 12, 23, 34, 67, 78, 89, 100]  # valido (diagonal 4x)
#j6 = [1, 12, 23, 34, 67, 78, 89, 100]  # valido (diagonal 4x)

js = [j1]
#js = [j1, j2, j3, j4, j5]

# Variaveis de controle para laco de qtd de coluna dentro do resultado
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0
cancel_res = False
lista_col = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'c7': 0,
             'c8': 0, 'c9': 0, 'c10': 0}

# Controle de numero de colunas aceitas
qtd_coluna_por_res = 2
diagonal_validacao = []
ha_diagonal = False

# loop para gerar resultados
for jogada in js:
    res_val = True
    # Loop para ler cada valor do resultado
    for num in jogada:
        if res_val is True:
            # Loop para encontrar em qual coluna o valor do resultado se encontra
            # apos isto abro o contador por coluna e armazeno em um
            # Dict "lista_col"
            for i in range(0, 5):
                if len(diagonal_validacao) == 0:
                    diagonal_validacao.append(num)
                else:
                    num = num + 11
                    diagonal_validacao.append(num)
            linha = 0
            num_v = 0
            indice_diagonal = 0
            for value in diagonal_validacao:
                for k, i in linJ.items():
                    for v in i:
                        if linha == 0 and num_v == 0:
                            if value == v:
                                linha = k
                                num_v = v
                        else:
                            if value == v:
                                if linha + 1 == k and v == num_v + 11:
                                    linha = k
                                    num_v = v
                                    res_val = False
                                else:
                                    res_val = True
            if res_val is True:
                print(f'Resultado OK >> {jogada}\n')
            elif set(diagonal_validacao).issubset(jogada):
                print(f'Achei o diagonal >> {diagonal_validacao}\n'
                      f'No resultado >> {jogada}\n')
            diagonal_validacao = []
