''' ALGORITIMOS SEQUENCIAIS'''

# Condicionais Compostas
x = int(input('Digite vlr inteiro: '))
y = int(input('Digite outro vlr: '))
if x > y:
    print('Seu 1° vlr é maior que o 2°')
    if (x % 2 == 0):
        print('E este valor é PAR')
    else:
        print('E este vlr é ÍMPAR')
elif x < y:
    print('Seu 2° vlr é maior que o 1°')
    print('Seu 1° vlr é maior que o 2°')
    if (y % 2 == 0):
        print('E este valor é PAR')
    else:
        print('E este vlr é ÍMPAR')

# Operadores boleanos:
'''Sequencia de calculo do python
1 - parenteses
2 - operadores aritiméticos de potencia ou raiz
3 - operadores de multiplicacao, divisao e modulos
4 - operadores de adição e subtracao
5 - relacionais
6 - lógicos NOT
7 - logicos AND
8 - logicos OR
9 - Atribuições
'''
# Condicionais Alinhadas