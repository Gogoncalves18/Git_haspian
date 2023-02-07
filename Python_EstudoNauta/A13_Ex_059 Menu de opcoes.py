maior_num = 0
num_1 = int()
num_2 = int()
opcao_user = int()
num_1 = int(input('Insira um numero qualquer: '))
num_2 = int(input('Insira mais um numero qualquer: '))
print('\n{:<15}{:^20}{:>15}'.format('-_-'*10,'MENU DE OPCOES PARA OPERADORES','-_-'*10))
print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do Programa
''')
print('\n{:<15}'.format('-_-'*60))
while True:
    opcao_user = int(input('Qual opcao vc deseja? '))
    if opcao_user > 5 or opcao_user < 1:
        print('Digite um numero entre 1 e 5!!')
        continue
    elif opcao_user == 5:
        break
    elif opcao_user == 1:
        print('\nA soma dos de {} e {} tem resultado {}.'.format(num_1, num_2,(num_2 + num_1)))
    elif opcao_user == 2:
        print('\nA mutiplicacao de {} com {} tem resultado {}.'.format(num_1, num_2,(num_2 * num_1)))
    elif opcao_user == 3:
        maior_num = num_1
        if maior_num < num_2:
            maior_num = num_2
        print('\nO maior numero entre {} e {} é {}.'.format(num_1, num_2,maior_num))
    elif opcao_user == 4:
        print('\nInsira abaixo os novos numeros:')
        num_1 = int(input('Insira um numero qualquer: '))
        num_2 = int(input('Insira mais um numero qualquer: '))
        
    