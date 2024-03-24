import random
nam1 = str(input('Digite o primeiro aluno: '))
nam2 = str(input('Digite o segundo aluno: '))
nam3 = str(input('Digite o terceiro aluno: '))
nam4 = str(input('Digite o quarto aluno: '))
lista = [nam1, nam2, nam3, nam4]
print('O aluno escolhido foi, {}.'.format(lista[(random.randint(0, 3))]))
