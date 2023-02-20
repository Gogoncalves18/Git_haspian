#Pegar n entradas do usuario e montar uma lista de pares e outra de impar
lst_num=[]
lst_par=[]
lst_impar=[]
while True:
    lst_num.append(int(input('\nDigite um numero: ')))
    sair=str(input('\nQuer continuar? [S] / [N]')).upper()[0]
    while sair not in 'SN':
        sair=str(input('\nDIGITE APENAS [S] / [N]')).upper()[0]
    if sair == 'N':
        break
print(f'\nLista digitada foi {lst_num}')
for v in lst_num:
    if v % 2 == 0:
        lst_par.append(v)
    else:
        lst_impar.append(v)
print(f'Temos uma lista par composta por {lst_par}')
print(f'Temos uma lista impar composta por {lst_impar}')