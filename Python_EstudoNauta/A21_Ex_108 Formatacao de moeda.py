'''Formatação de moeda usando um módulo Moeda dentro de um pacote
 de Modulos_Uteis'''
from Modulos_Uteis import moeda, cores

num = input('Digite um valor para ser formatado para moeda: ')
cores.titulo(moeda.moeda(num), 2)
print(cores.texto(moeda.moeda(num), 2))
print(moeda.moeda(num))
