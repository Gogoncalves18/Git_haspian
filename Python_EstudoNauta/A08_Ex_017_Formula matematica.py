'''EXERCICIO PARA APLICAR FORMULA MATEMATICA USANDO IMPORTACAO DE MODULO'''
print (' <> '*20)
import math
CO = float(input('\nDigite o valor do Cateto Oposto => '))
CA = float(input('\nDigite o valor do Cateto Adjacente => '))
H = (CO ** 2 + CA ** 2) ** (1/2)
print ('\nCom base no valor digitado de CO={} e CA={}, a Hipotenusa é {}.'.format(CO,CA,math.hypot(CO,CA)))
print ('\nCom base no valor digitado de CO={} e CA={}, a Hipotenusa é {:.2f}.'.format(CO,CA,H))
print (H)