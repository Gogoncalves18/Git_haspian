import time 


def seq(revr=False, inic=0, fim=0, passo=0):
    print('-*-'*40)
    if revr == False and inic == 0: 
        for c in range(0,11):
            print(c, end=', ', flush=True)
            time.sleep(0.5)
        print()
    elif revr == True and inic == 0:
        for c in range(10,-1,-1):
            print(c, end=', ', flush=True)
            time.sleep(0.5)
        print()
    elif inic != 0:
        for c in range(inic,fim+1,passo):
            print(c, end=', ', flush=True)
            time.sleep(0.5)
        print()
    print('-*-'*40)

seq()
seq(revr=True)
seq(inic=2, fim=10, passo=2) 