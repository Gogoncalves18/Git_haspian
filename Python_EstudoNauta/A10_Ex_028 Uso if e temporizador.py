import random
import time

print('-_-'*30)
print('\nVou pensar em um numero entre 0 e 5. Tente adivinhar!\n')
n_mac = random.randint(0, 5)
n_hum = int(input('\nQual numero eu pensei? '))
print('-_-'*30)
print('\nProcessando...')
time.sleep(3)
if n_hum == n_mac:
    print('\nParabéns! Vc Acertou!')
else:
    print('\nVc errou! O numero que eu pensei foi {}'.format(n_mac))
