lanche = ('burger', 'suco', 'pizza', 'pudim')
# Tupla tem parenteses e é imutavel
print(lanche)  # apresenta a tupla
print(lanche[2])  # pega uma posicao da tupla
print(lanche[-1])  # pega uma posicao da tupla de tras para frente

# rodo a lista para cada item em cada linha do print
for c in lanche:
    print(f'\nLISTA CORRIDA {c}')
print(f'\nTemos {len(lanche)} ingredientes!!!')
# leio o comprimento da tupla

# Conto os itens da tupla e identifico o item
for id in range(0, len(lanche)):
    print(f'Temos o ID {id}-{lanche[id]}')

# enumerate traz a posicao da tupla, podemos montar desta forma
for pos, papinha in enumerate(lanche):
    print(f'\nEu vou comer escolher a Opcao {pos} para comer {papinha}')

# para mostrar em ordem alfanetica
print(sorted(lanche))

# contar uma info dentro da tupla
a = (1, 3, 5)
b = (2, 5, 8)
c = a+b
print("")
print(c)
print(c.count(5))  # conta quantas vezes aparece o cinco
print(c.index(2))  # retorna a posicao do numero 2
