from typing import Any
from metodo_magico2 import Vector2


class Vector:
    def __init__(self, num) -> None:
        self.n1 = num
        self.pessoa = {'nome': 'Gustavo', 'idade': 41,}

    def __add__ (self, n):
        if not isinstance(n, int):
            n = int(n)
            print('aqui era texto e virou numero')
        return self.n1 + n
    
    def __eq__(self, n) -> bool:
        return True if self.n1 == n else False
    
    def __neg__(self):
        return f"Linha 15 - Manezao, ta no negativo"
    
    def __getitem__(self, k):
        if not k in self.pessoa.keys():
            return f'Não há esta chave - LINHA 20'
        return self.pessoa[k]
    
    def __setitem__(self, k, v):
        self.pessoa[k] = v

    def __call__(self, *args, **kwds):
        print(f'LINHA 30 = Fui chamado pela instancia com Args = {args} e Kwds = {kwds}')

    def __name__(self):
        return #f'Soyjo'
    
    def __main__(self):
        return
    
    

x = Vector(2)
y = Vector2(1)
print (x + "3")

print(x + 4)

print(x == 2)

print(-x)

print(x['sexo'])

x['sexo'] = 'M'

print(x['sexo'])

x()
x(2,3)
x(4,1, Nome='gg', parentesco = 'Maximo')

print(x.__name__)
print(y.__name__)

print(x.__main__)
print(y.__main__)
