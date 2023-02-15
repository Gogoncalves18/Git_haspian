#Aula de LISTAS
#comida=['Burger','Suco','Leite','Pizza','Pao','Xis']
comida=[]
print(f'LINHA 4 {type(comida)}')

#Adicionar item novo na lista, pode ser apenas um de cada vez
comida.append('Burger')
comida.append('Suco')

#Inserir item em uma posicao, so pode ocorrer se ha um item na posicao
print(f'LINHA 11 {comida}')
comida[1]='Pizza'
print(f'LINHA 13 {comida}')

#Para adicionar item em um posicao e empurrar o resto para frente
comida.insert(1,'Suco')
print(f'LINHA 17 {comida}')

#Apagar elementos da lista
print(f'LINHA 20 {comida}')
del comida[0] #apagar o burger
print(f'LINHA 22 {comida}')
comida.pop(1) #apaga a pizza, se nao der o indice, ele remove o ultimo elemento
print(f'LINHA 24 {comida}')

#Aumentar a lista para mais exemplos
comida=['Burger','Suco','Leite','Pizza','Pao','Xis', 'Leite']
print(F'linha 28 {comida}')

#Remover o valor de um item procurando pelo nome do item
comida.remove('Leite')
print(f'LINHA 32 {comida}') #Ele remove apenas a primeira ocorrencia

#Colocar os elementos em ordem
comida.sort() #ordem crescente
print(f'LINHA 35 {comida}')
comida.sort(reverse=True)
print(f'LINHA 38 {comida}')
