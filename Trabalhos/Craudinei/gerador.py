import sys
import time

def gera():
    #r = []
    for n in range(100):
        #r.append(n)
        yield n
        time.sleep(0.05)
    #return r

g = gera()

print(sys.getsizeof(g))



for v in g:
    print(v)