import datetime

print('\n{:<20} \033[1;30;40m{:^25}\033[m {:>20}'
      .format('-_-'*12, 'ANALISAR DATAS', '-_-'*12))
ano_in = int(input('\nDigite o ano para analisar se ele é BISSEXTO. \
                   Ou digite 0 (ZERO para trazer o ano atual): '))
if ano_in == 0:
    ano_act = datetime.date.today().year
    print('\n{}'.format(ano_act))
if ano_in % 4 == 0 and ano_in % 100 != 0 or ano_in % 400 == 0:  # para saber \
    # se o ano é bissexto tem: É um número divisível por 4,#  mas não é \
    # divisível por 100 E DEVE SER DIVISIVEL POR 400
    ano_anal = 'BISSEXTO'
else:
    ano_anal = 'Nao BISSEXTO'
print(ano_anal)
