#Ler num pares e soma-los. O final de 0 a 10 tem que ser 30.
soma = int(0)
for c in range(0,11):
    if c %2 ==0:
        soma += c
        print(c, end=' ')
print('\nA soma dos pares foi {}.'.format(soma))