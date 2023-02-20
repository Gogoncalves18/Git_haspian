#Crie um programa que leia varias numeros ate que o usuario pare
#Mostre se ha o numero 5 nele
#Mostre quantos elementos tem
#Mostre de forma decrescente a lista
lst_num=[]
saida=False
while saida is False:
    lst_num.append(int(input('\nDigite um numero inteiro: ')))
    resp=str(input('VC QUER CONTINUAR? [S] ou [N]')).upper()[0]
    if resp == 'S':
        continue
    elif resp == 'N':
        break
    elif resp not in 'SN':
        while True:
            print('\nVC NAO DIGITOU CORRETAMENTE')
            resp=str(input('VC QUER CONTINUAR? [S] ou [N]')).upper()[0]
            if resp in 'SN':
                saida=True
                break
print(f'\nA lista digitada em ordem decrescente foi {sorted(lst_num,reverse=True)}')
print(f'\nO numero 5 foi encontrado {lst_num.count(5)}X')
print(f'\nNesta lista temos {len(lst_num)} elementos!')




    