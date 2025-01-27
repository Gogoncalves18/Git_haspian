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
# [1, 12, 23, 34, 45]
# [28, 39, 50, 51, 62],
# [3, 14, 25, 36, 47]
# item 1 = valido
# item 2 = invalido
# item 3 = valido
res_diagonal = [
                [1, 12, 23, 36, 46],
                [3, 14, 25, 36, 47],
                [28, 39, 50, 51, 62]
                ]

for diagonal in res_diagonal:
    id_elem_diagonais = 0
    max_seq_diagonal = 4
    existe_diagonal = False
    match_diagonal = False
    linha = 0
    col = 0
    seq_diagonal = 0
    num_jogada_anterior = 0
    for num_jogada in diagonal:
        for linha_jogada, valores_lin in linJ.items():
            if existe_diagonal is False:
                if existe_diagonal is False and match_diagonal is False:
                    for valor_linJ in valores_lin:
                        if valor_linJ == num_jogada:
                            if col == 0 and linha == 0:
                                linha = linha_jogada
                                col = valores_lin.index(valor_linJ+1)
                                match_diagonal = True
                                num_jogada_anterior = num_jogada
                                break
                            else:
                                try:
                                    valores_lin.index(valor_linJ) in valores_lin
                                except ValueError:
                                    seq_diagonal = 0
                                    match_diagonal = False
                                    linha += 1
                                    col += 1
                                else:
                                    try:
                                        linha_jogada == linha + 1 and valores_lin.index(valor_linJ + 1) == col + 1
                                    except ValueError:
                                        # match_diagonal = False
                                        linha += 1
                                        col += 1
                                        seq_diagonal = 0
                                    else:
                                        if num_jogada_anterior + 11 == num_jogada:
                                            seq_diagonal += 1
                                            match_diagonal = False
                                            linha += 1
                                            col += 1
                                            num_jogada_anterior = num_jogada
                                        else:
                                            seq_diagonal = 0    
                                            match_diagonal = False
                                            linha += 1
                                            col += 1
                                            num_jogada_anterior = num_jogada
                                        break
                    if seq_diagonal >= max_seq_diagonal:
                        existe_diagonal = True
                        break
                else:
                    if match_diagonal is True:
                        match_diagonal = False
                        break
    if existe_diagonal is False:
        print(diagonal)    
