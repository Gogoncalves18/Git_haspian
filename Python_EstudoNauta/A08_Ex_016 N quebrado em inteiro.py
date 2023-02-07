'''EXEMPLO PARA ARRENDONDAR NUMEROS QUE SAO QUEBRADOS '''
import math
num = float(input('\nDigite qq n com casas apos virgula => '))
print ('\nO N digitado foi {} e sua parte inteira é {}.'.format(num,math.floor(num)))
print ('\nO N digitado foi {} e sua parte inteira é {:.0f}.'.format(num,num))
print ('\nO N digitado foi {} e a sua parte inteira é {}.'.format(num, int(num)))