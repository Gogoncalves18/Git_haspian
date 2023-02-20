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

#Copia de dados
lst_comida_1=[]
lst_comida_2=[]
lst_comida_1.append(comida[:3])
lst_comida_1.append(comida[3:])
print(f'LINHA 44 {lst_comida_1}')
print(f'LINHA 46 - Comp da lista - {len(lst_comida_1)}')
print(f'LINHA 47 - Comp do primeiro item da lista - {len(lst_comida_1[0])}')
lst_comida_1.insert(0,(2,1))
print(f'LINHA 49 Posso validar se é lista {type(lst_comida_1[0])}')
print(f'LINHA 50 {lst_comida_1}')
print(f'LINHA 51 {lst_comida_1[1][0]}') #Selecionar o segundo grupo e printar a primeira comida
