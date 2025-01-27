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
j1 = [1, 2, 3, 4, 12, 13, 14, 23, 24, 25, 34, 35]  # invalido (diagonal 5x)
j2 = [28, 39, 50, 61, 72, 83]  # valido
j3 = [2, 13, 24, 35, 57, 68]  # valido (com um pulo)
j4 = [1, 12, 23, 34, 56, 67, 78, 89, 100]  # invalido (diagonal 5x)
j5 = [1, 12, 23, 34, 67, 78, 89, 100]  # valido (diagonal 4x)
# j6 = [1, 12, 23, 34, 67, 78, 89, 100]  # valido (diagonal 4x)

jogos = [j1]

num_jogada = 3
existe_diagonal = False


def diagonal(jogada):
    '''Funcao para gerar possibilidade de diagonais
    sem validar se ela esta em uma unica linha de 
    diagonal'''
    diagonal_validacao = []
    posiveis_diagonais = []
    for num in jogada:
        # Loop para encontrar em qual coluna o valor do resultado se encontra
        # apos isto abro o contador por coluna e armazeno em um
        # Dict "lista_col"
        for i in range(0, 5):
            if len(diagonal_validacao) == 0:
                diagonal_validacao.append(num)
            else:
                num = num + 11
                diagonal_validacao.append(num)
        posiveis_diagonais.append(diagonal_validacao)
        diagonal_validacao = []
    return posiveis_diagonais


for jogo in jogos:
    res_diagonal = diagonal(jogo)
    print(res_diagonal)
'''
for linha_jogada, valores_lin in linJ.items():
    if existe_diagonal is False:
        for valor_linJ in valores_lin:
            if valor_linJ == num_jogada:
                print(f'ACHEI >> {num_jogada} em (Linha {linha_jogada} e coluna {valores_lin.index(valor_linJ+1)})')
                existe_diagonal = True
                break
    else:
        break
'''