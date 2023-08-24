import os
import sys
from calc_tempo import Tempo
from calc_tam_File import formata_tamanho
import cores
import config_cmd

tam_raiz = 0
tam_pasta = 0
tam_total = 0

#Definicao da SO que roda o app
if sys.platform.startswith('win32'):
    ponto_zero = 'c:\\'
    sep_OS_act = '\\' #Variavel para puxar o separador de caminho

elif sys.platform.startswith('linux'):
    ponto_zero = '/'
    sep_OS_act = '/' #Variavel para puxar o separador de caminho


comp_name = os.uname().nodename #Nome do computador que roda o app
user_name = os.environ['LOGNAME'] #carrego de uma string em formato de dict, o nome do user logado
user_local = os.environ['HOME'] #Endereco origem do user logado
test = os.environ
print(test)


walk = Tempo('Leitura por Walk')
walk.tIni()

def arqs():
    for pastas, subpastas, arqs in os.walk(user_local): 
        for subpasta in subpastas:
            yield pastas, subpasta

walk.tFim()            
    
ler_p = Tempo('Ler Pasta')
ler_p.tIni()

ler_pastas = arqs()

ler_p.tFim()

full_Path_LocalData = ''
full_Path_Cache = ''

tr = Tempo('Raiz')
tr.tIni()
for raiz, pasta in ler_pastas:
    tam_raiz += sys.getsizeof(raiz)
    tam_pasta += sys.getsizeof(pasta)
    tam_total += tam_raiz + tam_pasta

    if pasta == 'UserCache':
        comp_Pastas = raiz.split(os.path.sep)
        if 'Dassault Systemes' in comp_Pastas:
            print(f'\nACHEI O CACHE EM => {os.path.join(raiz, pasta)}')
            full_Path_Cache = os.path.join(raiz, pasta)
            print(os.listdir(full_Path_Cache))
            burning_cache = os.path.join(full_Path_Cache, os.listdir(full_Path_Cache)[0])

    elif pasta == 'DassaultSystemes':
        comp_Pastas = raiz.split(os.path.sep)
        if 'LOCALAPPDATA' in comp_Pastas:
            print(f'\nACHEI O LOCALDATA EM => {os.path.join(raiz, pasta)}')
            full_Path_LocalData = os.path.join(raiz, pasta)
           
       
tr.tFim()

val_path = Tempo('validacao Caminho')
val_path.tIni()

if os.path.exists(full_Path_Cache) and len(os.listdir(full_Path_Cache)) > 0:
    print(f'\nDeletei cache => {burning_cache}')
    #os.unlink(burning_cache)
else:
    print(f'\n NENHUM ARQ DE CACHE ENCONTRADO')  

if os.path.exists(full_Path_LocalData):
    print(f'\nDeletei localData=> {full_Path_LocalData}')
    #shutil.rmtree(full_Path_LocalData)
else:
    print(f'\n NENHUM ARQ DE LOCALDATA ENCONTRADO')  

val_path.tFim()

print(f'\nTAMANHO TOTAL DA RAIZ = {formata_tamanho(tam_raiz)}')
print(f'\nTAMANHO TOTAL DA PASTA = {formata_tamanho(tam_pasta)}')
print(f'\nTAMANHO TOTAL DA TOTAL = {formata_tamanho(tam_total)}')  

print(f'\n=======================================================================================')
while True:
    #config_cmd.conf_existe
    cores.titulo('OPÇÔES DE TAREFAS', 2)
    print(f'{cores.texto("[ 1 ] ", 2)}{cores.texto("PROD SKA", 3)}')
    print(f'{cores.texto("[ 2 ] ", 2)}{cores.texto("CRAU SKA", 3)}')
    print(f'{cores.texto("[ 3 ] ", 2)}{cores.texto("CRAU MODULAR", 3)}')
    print(f'{cores.texto("[ 4 ] ", 2)}{cores.texto("ENCERRAR", 3)}')

    print()
    opcao = int(input(cores.texto("Digite uma opção: ", 2)))

    if opcao == 1:
        config_cmd.arq_cmd('prodska')
    elif opcao == 2:
        config_cmd.arq_cmd('crauska')
    elif opcao == 3:
        config_cmd.arq_cmd('craumod')
    elif opcao == 4:
        break

