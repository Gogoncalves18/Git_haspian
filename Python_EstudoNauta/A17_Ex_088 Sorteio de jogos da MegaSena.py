# Programa deve pedir o numero de jogo para o usuarios e sortear 6
# numeros usando listas
import random

print(f'{"-_-"*20} SORTEIO PARA MEGA {"-_-"*20}')
sorteio_temp = []  # Lista temporaria para receber e passar vlr e
# limpar
sorteio_final = []
qtd_jogos = int(input('\nQuantos jogos vc deseja: '))
for j in range(0, qtd_jogos):  # N jogos que o usuario quer que
    # calcule
    sorteio_temp.append(random.sample(range(1, 60), 6))
    # TIPO DE RANDOM QUE RETORNA 6 VALORES QUE NAO REPETEM
    sorteio_final.append(sorteio_temp[0])  # Fatiamento da copiada
    # para lista final
    sorteio_temp.clear()  # limpeza da lista temporaria
    print(f'\nSoteio N_{j+1} => {sorted(sorteio_final[j])}')
