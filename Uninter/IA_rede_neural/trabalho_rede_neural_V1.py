import dis


def convert_assemb():

    pesos = [0.563157895, 0.503157895, -0.281052632, -0.324210526,	0.661052632, -0.189473684]
    amostras = [[3, 6, -1, 9, -1, 6, -1],
                [4, 2, 3, -1, -2, 9, -1],
                [2, 2, 0, 1, -2, 7, -1],
                [0, 1, 0, 4, -1, 1, -1],
                [3, 3, 3, 5, 0, 3, -1],
                [-1, -1, 9, 3, 8, -1, -1],
                [2, 7, 4, 2, 6, -2, 1],
                [0, 0, 0, 8, 9, 4, 1],
                [4, 1, 6, 4, -2, -2, -1],
                [-2, 2, -1, 1, -2, -1, -1],
                [4, -2, 4, 2, 0, 4, -1],
                [-2, -2, 7, 2, -1, 5, -1],
                [-1, 2, -1, -2, 9, -2, 1],
                [1, -2, 0, -1, -2, 4, -1],
                [-2, 5, -2, 8, 1, 9, -1],
                [-1, 8, 7, 0, 8, -1, 1],
                [5, -2, 5, -1, 8, 9, 1],
                [9, -1, -2, -2, 6, 7, 1],
                [-1, 2, 6, 5, 1, 5, -1]
                ]

    fx_ativ = 0
    len_amostras = len(amostras)
    contagem_leitura = 0
    while True:
        if contagem_leitura < len_amostras:
            line = amostras[contagem_leitura]
            d1 = (float(line[0])*float(pesos[0])) +\
                (float(line[1])*float(pesos[1])) +\
                (float(line[2])*float(pesos[2])) +\
                (float(line[3])*float(pesos[3])) +\
                (float(line[4])*float(pesos[4])) +\
                (float(line[5])*float(pesos[5])) + (-1)
            if d1 >= 0:
                fx_ativ = 1
                print(f'Saída de Ativação: {fx_ativ} => Mantenha Produção')
            else:
                fx_ativ = -1
                print(f'Saída de Ativação: {fx_ativ} => DESATIVAR ESTEIRAS')

            contagem_leitura += 1
        else:
            break


dis.dis(convert_assemb)
