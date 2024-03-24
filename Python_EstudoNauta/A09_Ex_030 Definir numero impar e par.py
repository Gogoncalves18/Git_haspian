print('\n{:<10} \033[1;30;47m{:^25}\033[m {:>10}'
      .format('-_-'*10, 'Definir Par e Impar', '-_-'*10))
num = float(input('\nDigite um numero inteiro qualquer: '))
if num % 2 == 0:
    t_num = 'PAR'
else:
    t_num = 'IMPAR'
print('\nO numero digitado é {}'.format(t_num))
print('\n{:<15} \033[1;47;30m{:^15}\033[m {:>15}'
      .format('_-_'*10, 'FIM', '_-_'*10))
