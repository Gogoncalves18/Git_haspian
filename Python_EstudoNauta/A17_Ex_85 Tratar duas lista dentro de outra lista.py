# Pedir 7 numeros inteiros e colocalos em duas listas separadas
# dentro de outra lista.
# Depois apresente cada lista em de par e impar em ordem crescente
lst_temp = []
lst_par = []
lst_impar = []
lst_main = []
for p in range(0, 7):
    num = int(input('\nDigite um valor: '))
    if num % 2 == 0:
        lst_par.append(num)
    else:
        lst_impar.append(num)
lst_main.append(lst_par[:])
lst_main.append(lst_impar[:])
print(f'\nLista Principal {lst_main}')
print(f'''\nA Lista par em ordem crescente {sorted(lst_main[0])}
       e a impar em ordem crescente {sorted(lst_main[1])}''')
