titulo = 'TABUADA V3.0'
esp_central = len(titulo)
rash = '-_-' * (int(((100-esp_central)-2)/6))
print(f'{rash}{titulo}{rash}')
while True:
    num = int(input('\nQual numero vc quer a tabuada? '))
    for n in range(1, 11):
        multi = num*n
        print(f'{num} x {n} = {multi}')
    sair = (str(input('Clique [C] para continuar\
ou [Q] para sair!'))).upper()[0]
    if sair == 'Q':
        break
    elif sair == 'C':
        continue
    else:
        print('Digite uma saida valida')
