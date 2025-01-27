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

jogo = (55, 57, 66, 69, 77, 88)
seq_diagonal = 4
valor_inicial = 0
diagonal_validada = False

for valor in jogo:
    cont_diagonal = 1
    for k, v in linJ.items():
        if valor in v:
            coluna = v.index(valor) + 1
            break
    while coluna < 10:
        if (valor + 11) in jogo:
            valor = valor + 11
            # cont_diagonal += 1
            for k, v in linJ.items():
                if valor in v:
                    coluna = v.index(valor) + 1
                    cont_diagonal += 1
                    break
        else:
            break
    if cont_diagonal >= seq_diagonal:
        print(f'SEQ anulada {jogo}')
        break
    else:
        diagonal_validada = True

if diagonal_validada:
    print(f'Resultado OK {jogo}')    
            
