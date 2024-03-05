'''ESTRUTURAS DE REPETICAO'''
vlr = 0
qt_voltas = int(input('Adicione o nº de voltas: '))
while (vlr <= qt_voltas):
    vlr += 1
    msg = f'Lá foi mais {vlr} volta'
    print(msg)

for letter in msg:
    print(f'Letra: {letter}')
