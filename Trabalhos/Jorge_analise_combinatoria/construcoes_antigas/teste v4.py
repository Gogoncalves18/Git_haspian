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
j1 = [1, 2, 3, 13, 15, 17]  # invalido c3(2x)
j2 = [1, 2, 3, 14, 15, 17]  # valido
j3 = [5, 6, 25, 38, 60, 89]  # invalido c5(2x)
j4 = [2, 33, 56, 57, 98, 100]  # valido
j5 = [6, 17, 26, 36, 67, 96]  # invalido c6(4x) e c7(2x)
js = [j1, j2, j3, j4, j5]

# Variaveis de controle para laco de qtd de coluna dentro do resultado
c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0
cancel_res = False
lista_col = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0, 'c7': 0,
             'c8': 0, 'c9': 0, 'c10': 0}

# Controle de numero de colunas aceitas
qtd_coluna_por_res = 2

# loop para gerar resultados
for jogada in js:
    # Loop para ler cada valor do resultado
    for num in jogada:
        # Loop para encontrar em qual coluna o valor do resultado se encontra
        # apos isto abro o contador por coluna e armazeno em um
        # Dict "lista_col"
        for lin, values in linJ.items():
            if num in values:
                pos = (values.index(num) + 1)
                if pos == 1:
                    c1 += 1
                    lista_col['c1'] = c1
                elif pos == 2:
                    c2 += 1
                    lista_col['c2'] = c2
                elif pos == 3:
                    c3 += 1
                    lista_col['c3'] = c3
                elif pos == 4:
                    c4 += 1
                    lista_col['c4'] = c4
                elif pos == 5:
                    c5 += 1
                    lista_col['c5'] = c5
                elif pos == 6:
                    c6 += 1
                    lista_col['c6'] = c6
                elif pos == 7:
                    c7 += 1
                    lista_col['c7'] = c7
                elif pos == 8:
                    c8 += 1
                    lista_col['c8'] = c8
                elif pos == 9:
                    c9 += 1
                    lista_col['c9'] = c9
                elif pos == 10:
                    c10 += 1
                    lista_col['c10'] = c10
    # Apos contar todas as colunas, percorro o dict "lista_col" para validar
    # se o resultado e valido
    for k_col, v_col in lista_col.items():
        # Se o laco entrar aqui, o resultado nao e valido
        if v_col >= qtd_coluna_por_res:
            cancel_res = True
            # print(f'Resultado invalida => Res {jogada} - Num Colunas '
            #      f'{lista_col}')
    # Nesta condicional, geramos apenas os resultados validos
    if cancel_res is False:
        print(f'Resultado valida => Res {jogada} - Num Colunas {lista_col}')
        # Zeramento dos contadores para analise de novo resultado
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0
        lista_col = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0,
                     'c7': 0, 'c8': 0, 'c9': 0, 'c10': 0}
    # Condicional quando o resultado falha por causa do numero de colunas
    # e zeramento dos contadores
    else:
        lista_col = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0, 'c6': 0,
                     'c7': 0, 'c8': 0, 'c9': 0, 'c10': 0}
        c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0
        cancel_res = False
