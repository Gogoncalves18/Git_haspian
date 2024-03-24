# Digitar 4 numeros pra entrar em uma tupla e depois analisar quantas
# vezes o 9 aparece, qual a posicao que o 3 aparece quais sao os
# numeros pares da tupla. OBS>: nao fiz tratamento de expection

n = (int(input('Digite um numero: ')), int(input('Digite um numero: ')),
     int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {n.count(9)}x!')
print(f'O valor 3 apareceu na posicao {n.index(3)}')
print('Os valores pares digitados foram: ', end=" ")
# O 'END=" "' é para não pular para linha do próimo print
for i in n:
    if i % 2 == 0:
        print(i, end=' - ')
    else:
        pass
print('')
