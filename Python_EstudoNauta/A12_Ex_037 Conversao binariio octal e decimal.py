print('\n{:<20} \033[7;33;41m{:^25}\033[m{:>20}'.format('-_-'*15, 'INICIO DO PROGRAMA', '-_-'*15))
num = int(input('\nDigite numero inteiro que vc quer converter: '))
print ('\n1 - Para converter para BINARIO')
print ('2 - Para converter para OCTAL')
print ('3 - Para converter para HEXADECIMAL')
num_choiced = int(input('\n\033[1;30;41m{}\033[m'.format('Escolha a opcao de 1 a 3 => ')))
num_diged = True
while num_diged:
    if num_choiced >=1 and num_choiced <=3:
        num_diged = False
        if num_choiced == 1:
            print('\n{} convertido para BINARIO é igual {}'.format(num, bin(num)))
        elif num_choiced == 2:
            print('\n{} convertido para OCTAL é igual {}'.format(num, oct(num)))
        else:
            print('\n{} convertido para HEXADECIMAL é igual {}'.format(num, hex(num)))
    else:
        print('\n\033[1;33;40m{}\033[m Voce escolheu uma opcao inexistente! Tente novamente'.format('ERRO! '))
        num_choiced = int(input('\n\033[1;30;41m{}\033[m'.format('Escolha a opcao de 1 a 3 => ')))
print('\n{:<20} \033[7;33;41m{:^25}\033[m{:>20}'.format('-_-'*15, 'FIM DO PROGRAMA', '-_-'*15))