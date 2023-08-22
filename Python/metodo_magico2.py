class Vector2:
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