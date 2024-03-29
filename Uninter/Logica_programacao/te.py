'''vlrs_prod = {'CP': [9, 14, 18], 'AC': [11, 16, 20]}

ped = [{'prod': 'CP', 'tam': 'P'}, {'prod': 'AC', 'tam': 'G'}]

vlr_total = 0
for i in ped:
    if i['tam'] == 'P':
        t = 0
    elif i['tam'] == 'M':
        t = 1
    else:
        t = 2
    vlr_total += vlrs_prod[i['prod']][t]
print(vlr_total)

vlrs_prod = {'DIG': 1.10, 'ICO': 1, 'IBO': 0.40, 'FOT': 0.20}

print(vlrs_prod['DIG'])'''


def proc_dados(chave):
    for i in lista_livro:
        if i['id'] == int(chave):
            print('*' * 48)
            for k, v in i.items():
                print(f'* {k:<20} => {v:<20} *')
            print('*' * 48,)


lista_livro = [{
                'id': 1,
                'nome_l': 'Pega no meu!',
                'autor_l': 'GOG',
                'editora': 'TNC'
                },
               {
                'id': 2,
                'nome_l': 'CHupa!',
                'autor_l': 'VAL',
                'editora': 'Taradas'
                }]

'''for i in lista_livro:
    print('*' * 48)
    for k, v in i.items():
        print(f'* {k:<20} => {v:<20} *')
    print('*' * 48,)'''
# cons_pers_user = input('Pesquisar: ')
# proc_dados(cons_pers_user)
print(lista_livro)
sair = False
while True:
    try:
        id_user_remov = int(input('\nID de livro para deletar: '))
    except ValueError:
        print('\nDigite um ID existente!')
    else:
        cont = 0
        for i in lista_livro:
            print(i)
            if i['id'] == id_user_remov:
                print(f'achei => {i['nome_l']}')
                print(lista_livro)
                del lista_livro[cont]
                print(lista_livro)
            else:
                cont += 1
    break
