import datetime
ano_atual = int(datetime.date.today().year)
ano_born = int(input('\nQual o ano de seu nascimento? '))
if (ano_atual - ano_born) == 19:
    print('\nVoce esta com 18 anos, precisa se alistar imediatamente!')
elif (ano_atual-ano_born) > 19:
    print('\nVoce ja passou {} anos de seu alistamento, voce esta presso!'.format(((ano_atual-ano_born)-19)))
else:
    print('\nTakerese man, ainda falta {} anos para ferrarmos com a sua vidinha!'.format((19-(ano_atual-ano_born))))
