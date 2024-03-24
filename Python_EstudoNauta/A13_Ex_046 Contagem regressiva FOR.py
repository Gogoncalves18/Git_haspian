import time

time.sleep(1)
for c in range(10, -2, -1):
    # O 10 é a tamanho do range, -2 é o final do range para acabar em -1
    # e o -1 é o passo regressivo do range
    time.sleep(1)
    print(c)
