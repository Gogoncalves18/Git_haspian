print('\n{:<20} \033[7;33;41m{:^25}\033[m {:>20}'.format('-_-'*12, 'SIMULACAO\
                                                    EMPRESTIMO', '-_-' * 12))
vlr_emp = int(input('\nInsira o valor do imovel a ser financiado =>'))
qdt_anos = int(input('\nEm quantos anos vc quer financiar? '))
vlr_sal = int(input('\nQual o valor de sua renda financeira? '))
tmp = int(qdt_anos*12)
cap_ini = vlr_emp
tx = 0.01
mont_emprestimo = cap_ini*((1+tx)**tmp)
vlr_parc = float(mont_emprestimo/tmp)
if (vlr_sal*0.3) >= vlr_parc:
    print('\nCREDITO APROVADO! Seu financiamento sera de {} parcelas,\
           com valor de R${:.2f} por parcela'.format(tmp, vlr_parc))
else:
    print('\nCREDITO REPROVADO! Infelizamente sua renda de R${:.2f} nao \
          comporta a prestacao de R${:.2f}'.format(vlr_sal, vlr_parc))
print('\n{:<20} \033[7;33;41m{:^25}\033[m {:>20}'.format('_-_'*12, 'FIM\
                                                    SIMULACAO', '_-_' * 12))
