import math
import random
import emoji
num = int(input('digite num'))
raiz =math.sqrt(num)
print ('A raiz de {} é igual ao valor arrendondado de {}'.format(num, math.ceil(raiz)))
n_sorte = random.randint(0,10)
print ('Seu número da sorte é {}.'.format(n_sorte))
print (emoji.emojize('tamao que te mandaram :sunglasses:'))
 