num_s=[]
for ask in range(0,5):
    n=int(input(f'Digite um numero: '))
    if ask == 0 or n > num_s[-1]: #O -1 pega o ultimo da lista
        num_s.append(n)
    else:
        pos = 0 # posicao 0 para ter um ponto de partida para o while varrer a lista
        while pos < len(num_s):
            if n <= num_s[pos]:
                num_s.insert(pos,n)
                break
            pos+=1
print(f'A lista digitada => {num_s}')
    