da_pasta = ['P1', 'P2']
dados1 = ['1a', '1b', '1c']
dados2 = ['2a', '2b', '2c']
list_leitura = []
dict_leitura = {}
list_lib = []

for p in da_pasta:
    dict_leitura.clear()
    list_leitura.clear()
    if (da_pasta.index(p)) == 0:
        dict_leitura['Nome Pasta'] = p
        for i in dados1:
            list_leitura.append(i)
        dict_leitura['Vlrs_Pasta'] = list_leitura.copy()
    elif (da_pasta.index(p)) == 1:
        dict_leitura['Nome Pasta'] = p
        for i in dados2:
            list_leitura.append(i)
        dict_leitura['Vlrs_Pasta'] = list_leitura.copy()
    list_lib.append(dict_leitura.copy())
print()
print(f'========>  {list_lib}')
