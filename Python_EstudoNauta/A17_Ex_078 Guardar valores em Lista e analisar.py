# Guardar 5 valores na lista
# Apresentar os valores
# Analisar qual o maior Valor e sua posicao
# Analisar o menor valor e sua posicao

# sem pegar posicoes
'''
vlrs=[]
for vlr in range(1,6):
    vlr=int(input('Digite um vlr inteiro: '))
    vlrs.append(vlr)
print(f'\nOs valores digitados foram {vlrs}')
vlrs.sort()
print(f'\nO menor valor digitado foi {vlrs[0]}')
vlrs.sort(reverse=True)
print(f'\nMaior valor digitado foi {vlrs[0]}')
print('')
'''
# Pegando posicoes

vlrs = []
n_max = 0
n_min = 0
for vlr in range(0, 6):
    vlrs.append(int(input('Digite um vlr inteiro: ')))
    if vlr == 0:
        n_min = n_max = vlrs[vlr]
    else:
        if vlrs[vlr] < n_min:
            n_min = vlrs[vlr]
        elif vlrs[vlr] > n_max:
            n_max = vlrs[vlr]
print(f'\nOs valores digitados foram: {vlrs}')
print(f'''\nO MENOR valor encontrado foi {n_min} que esta na POS
      {vlrs.index(n_min)}''')
print(f'''\nO MAIOR valor encontrado foi {n_max} que esta na POS
      {vlrs.index(n_max)}''')
