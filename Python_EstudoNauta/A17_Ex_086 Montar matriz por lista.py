#Digitar 9 numeros e preencher uma matriz de 3x3 usando listas:
matrix=[[0,0,0],[0,0,0],[0,0,0]] #Crio o espaco reservado para os valores
for l in range(0,3): #Primeiro laco pega a primeira lista
    for c in range(0,3): #segundo laco pega os items da lista
        matrix[l][c]=int(input(f'Insira um valor para posicao {l},{c} da matriz: ')) #insiro os valores em cada posicao de cada lista
for l in range(0,3): #trabalho no print apenas para plotar os itens de cada lista em matriz
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()