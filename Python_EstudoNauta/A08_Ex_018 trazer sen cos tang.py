import math

ang = int(input('\nDigite um angulo inteiro para descobrir SEN, COS e TANJ: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)
print('Para o Angulo de {} temos os seguintes resultados:\
      \nSen = {:.2f}\nCos = {:.2f}\nTang = {:.2f}'.format(ang, sen, cos, tang))
