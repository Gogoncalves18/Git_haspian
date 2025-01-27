def validar_par_impar(jogo: tuple, linJ: dict, possib: int):
    # Zeramento do contador linhas
    lin1 = 0
    lin2 = 0
    lin3 = 0
    lin4 = 0
    lin5 = 0
    lin6 = 0
    lin7 = 0
    lin8 = 0
    lin9 = 0
    lin10 = 0
    # Zeramento do contador linhas par impar da linha 1 e 2
    lin1_par = 0
    lin1_impar = 0
    lin2_par = 0
    lin2_impar = 0
    lin3_par = 0
    lin3_impar = 0
    lin4_par = 0
    lin4_impar = 0
    lin5_par = 0
    lin5_impar = 0
    lin6_par = 0
    lin6_impar = 0
    lin7_par = 0
    lin7_impar = 0
    lin8_par = 0
    lin8_impar = 0
    lin9_par = 0
    lin9_impar = 0
    lin10_par = 0
    lin10_impar = 0
    
    # cada jodada trara uma sequencia de resultados dentro dos criterios
    for i in jogo:
        for k, v in linJ.items():
            if i in v:
                if i % 2 == 0:
                    if k == 1:
                        lin1 += 1
                        lin1_par += 1
                    elif k == 2:
                        lin2 += 1
                        lin2_par += 1
                    elif k == 3:
                        lin3 += 1
                        lin3_par += 1
                    elif k == 4:
                        lin4 += 1
                        lin4_par += 1
                    elif k == 5:
                        lin5 += 1
                        lin5_par += 1
                    elif k == 6:
                        lin6 += 1
                        lin6_par += 1
                    elif k == 7:
                        lin7 += 1
                        lin7_par += 1
                    elif k == 8:
                        lin8 += 1
                        lin8_par += 1
                    elif k == 9:
                        lin9 += 1
                        lin9_par += 1
                    elif k == 10:
                        lin10 += 1
                        lin10_par += 1
                else:
                    if k == 1:
                        lin1 += 1
                        lin1_impar += 1
                    elif k == 2:
                        lin2 += 1
                        lin2_impar += 1
                    elif k == 3:
                        lin3 += 1
                        lin3_impar += 1
                    elif k == 4:
                        lin4 += 1
                        lin4_impar += 1
                    elif k == 5:
                        lin5 += 1
                        lin5_impar += 1
                    elif k == 6:
                        lin6 += 1
                        lin6_impar += 1
                    elif k == 7:
                        lin7 += 1
                        lin7_impar += 1
                    elif k == 8:
                        lin8 += 1
                        lin8_impar += 1
                    elif k == 9:
                        lin9 += 1
                        lin9_impar += 1
                    elif k == 10:
                        lin10 += 1
                        lin10_impar += 1
         # Valida se nao ultrapassou a contagem de numeros por linha
    if lin1 < 6 and lin2 < 6 and lin3 < 6 and lin4 < 6\
    and lin5 < 6 and lin6 < 6 and lin7 < 6 and lin8 < 6\
    and lin9 < 6 and lin10 < 6:

        # Valida a contagem de par e impar aceito por linha
        if lin1_par < 6 and lin1_impar < 6 and lin2_par < 6 and lin2_impar < 6\
           and lin3_par < 6 and lin3_impar < 6 and lin4_par < 6 and lin4_impar < 6\
           and lin5_par < 6 and lin5_impar < 6 and lin6_par < 6 and lin6_impar < 6\
           and lin7_par < 6 and lin7_impar < 6 and lin8_par < 6 and lin8_impar < 6\
           and lin9_par < 6 and lin9_impar < 6 and lin10_par < 6 and lin10_impar < 6:
            return jogo
        else:
            print(f'JOGO {possib} Impar/Par falhou => {jogo}')
            return 0
    else:
        print(f'JOGO {possib} FORA QTD num por linha => {jogo}')
        return 0