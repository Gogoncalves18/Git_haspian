'''Faca um programa que tenha uma lista de chamada numeros
e duas funcoes samando sorteio() e somar().
A primeira funcao vai sortear 5 numeros e colocar dentro de uma lista
A segunda funcao vai somar todos os numeros pares sorteados da funcao anterior
'''
from random import randint

lst_num = []


def sorteio():
    for c in range(1, 6):
        lst_num.append(randint(0, 21))
    print(f'\nOs numeros sorteados foram: {lst_num}')


def somar():
    soma = 0
    for n in lst_num:
        if n % 2 == 0:
            soma += n
    print(f'\nA soma dos numeros pares dentro da lista {lst_num} é : \
{soma}')


# PROGRAMA PRINCIPAL
sorteio()
somar()
