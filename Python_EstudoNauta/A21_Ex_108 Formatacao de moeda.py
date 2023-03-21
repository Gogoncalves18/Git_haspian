'''Formatação de moeda usando um módulo Moeda dentro de um pacote de Modulos_Uteis'''
from Modulos_Uteis import moeda

num = input('Digite um valor para ser formatado para moeda: ')
print(moeda.moeda(num))