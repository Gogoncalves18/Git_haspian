import time
   
class Tempo():
    """
    - Necessário instanciar a classe com um nome no parametro, para identificar melhor o print
    - Chamar o metodo tIni() para ele pegar o tempo inicial antes da área a ser medida
    - Chamar o metodo tFim() para ele pegar o tempo final depois da área a ser medida
    """
    def __init__(self, nome, t_ini=0, t_fim=0):
        self.nome = nome
        self.t_ini = t_ini
        self.t_fim = t_fim

    def tIni(self):
        self.t_ini = time.time()
        #print(f'\nTEMPO INICIAL {self.t_ini}')

    def tFim(self):
        self.t_fim = time.time()
        #print(f'\nTEMPO FINAL {self.t_fim}')
        print(f'\nO TRECHO {self.nome} DEMOROU {self.t_fim-self.t_ini:.3f} segundos!!!!!!!')
