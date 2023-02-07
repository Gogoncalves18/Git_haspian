print ('-_-'*30)
fr = str(input('\nDigite seu nome completo para analise: '))
print ('\nAnalisando seu nome, vejo... ')
print ('\nSeu nome em maisculo fica assim: {}'.format(fr.upper()))
print ('\nSeu nome em minusculo fica assim: {}'.format(fr.lower()))
print ('\nSeu nome possui {} letras ao todo!'.format(len(fr)))
lst = fr.split()
print ('Seu primeiro nome e {} e ele possui {} letras!'.format(lst[0].upper(), fr.find(' ')))
 