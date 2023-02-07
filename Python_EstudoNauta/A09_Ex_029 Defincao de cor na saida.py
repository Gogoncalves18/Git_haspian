print ('\n{:<10} {:^15} {:>10}'.format('-_-'*10,'RADAR','-_-'*10))
vel = int(input('\nQual a velocidade do veículo? '))
if vel <= 80:
    print ('\nContinue dirigindo desta forma!')
if vel > 80 and vel <= 80*1.5:
    multa = (vel-80)*100
    print ('\n\033[1;37;43mMulta MENOR! Vc deve pagar R${:.2f}\033[m'.format(multa))
elif vel > 80*1.5:
    multa = (vel-80)*200
    print ('\n\033[1;31;41mMulta MAIOR! Vc deve para R${:.2f}\033[m'.format(multa))