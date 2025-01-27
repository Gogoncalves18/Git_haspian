def validar_coluna(sequencia_validada: tuple, qtd_coluna_por_res: int, possib: int, linJ: dict):
    # Variaveis de controle para laco de qtd de coluna dentro
    # do resultado
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = 0
    cancel_res = False
    lista_col = {'c1': 0, 'c2': 0, 'c3': 0, 'c4': 0, 'c5': 0,
                    'c6': 0, 'c7': 0, 'c8': 0, 'c9': 0, 'c10': 0}


    # Loop para ler cada valor do resultado
    for num in sequencia_validada:
        # Loop para encontrar em qual coluna o valor do resultado
        # se encontra
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
    # Apos contar todas as colunas, percorro o dict "lista_col"
    # para validar se o resultado e valido
    for k_col, v_col in lista_col.items():
        # Se o laco entrar aqui, o resultado nao e valido
        if v_col > qtd_coluna_por_res:
            cancel_res = True
            # print(f'Resultado invalida => Res {jogada} -
            # Num Colunas '
            #      f'{lista_col}')
    # Nesta condicional, geramos apenas os resultados validos
    if cancel_res is False:
        # print(f'Resultado valida => Res {jogada} ')
        return sequencia_validada
    else:
        print(f'Jogo {possib} com limite de numeros na coluna coluna => {sequencia_validada}')
        return 0
        