#Devemos percorrer os 10 melhores times posicionados, apresentar os 3 primeiros, os dois ultimos e a ordem alfabetica
rank_dos10=('gremio','palmeiras','flamengo','corinthias','atletico/MG',
            'internacional','santos','cruzeiro','bahia','fluminense')
print('')
print('-_-'*40)
print(f'Os Tres primeiros colocados sao: {rank_dos10[0:3]}')
print('')
print('-_-'*40)
print(f'Os Dois ultimos colocados sao: {rank_dos10[8:10]}')
print('-_-'*40)
print(f'Os times em ordem alfabetica: {sorted(rank_dos10)}')
print(f'O Inter esta na posicao {rank_dos10.index("internacional")+1}')
print('') 