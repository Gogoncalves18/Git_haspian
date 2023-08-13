import os
import sys
from calc_tempo import Tempo
from calc_tam_File import formata_tamanho

tam_raiz = 0
tam_pasta = 0
tam_total = 0

walk = Tempo('Leitura por Walk')
walk.tIni()

for pastas, subpastas, arqs in os.walk('/'): #Preciso definir se a entrada é Windows ou linux
    tam_raiz += sys.getsizeof(pastas)
    tam_pasta += sys.getsizeof(subpastas)
    tam_total += tam_raiz + tam_pasta
    for subpasta in subpastas:
        if subpasta == 'UserCache':
            comp_Pastas = pastas.split(os.path.sep)
            if 'Dassault Systemes' in comp_Pastas:
                print(f'ACHEI O ARQUIVO EM: {os.path.join(pastas, subpasta)}')
                end_User_cache = os.path.join(pastas, subpasta)
                print(f'AQUI TUDO QUE CONTEM DENTRO DELA => {os.listdir(end_User_cache)}')
                if len(os.listdir(end_User_cache)) > 0: 
                    print(f'AQUI SOMENTE O PRIMEIRO ARQUIVO DA LISTA => {os.listdir(end_User_cache)[0]}')
                    print(f'AQUI O CAMINHO COMPLETO COM O ARQUIVO => {end_User_cache+os.listdir(end_User_cache)[0]}')
                    cash_Local = end_User_cache + '/' + os.listdir(end_User_cache)[0]


    # for subpasta in subpastas:
    #     if subpasta == 'DassaultSystemes':
    #         comp_Pastas = pastas.split(os.path.sep)
    #         if 'LOCALAPPDATA' in comp_Pastas:
    #             print(f'ACHEI O ARQUIVO EM: {os.path.join(pastas, subpasta)}')
    #             local_Data_DS = os.path.join(pastas, subpasta)

walk.tFim()            
    
val_path = Tempo('validacao Caminho')
val_path.tIni()

if os.path.exists(end_User_cache) and len(os.listdir(end_User_cache)) > 0:
    print(f'\nCaminho do CACHE EXISTENTE')
    #os.unlink(cash_Local)
    
else:
    print(f'\n NENHUM ARQ DE CACHE ENCONTRADO')

val_path.tFim()


print(f'\nTAMANHO TOTAL DA RAIZ = {formata_tamanho(tam_raiz)}')
print(f'\nTAMANHO TOTAL DA PASTA = {formata_tamanho(tam_pasta)}')
print(f'\nTAMANHO TOTAL DA TOTAL = {formata_tamanho(tam_total)}')    


