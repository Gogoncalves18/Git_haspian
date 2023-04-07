class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.planos_disponiveis = ['basic', 'premium']
        self.filmes_basic = ['Susi e o Pone', 'Fogo na Caixa dAgua', 'Corri pelado', 'Pega no meu e diz que é teu'] #Esta lista só funcionou quando coloquei o self
        self.filmes_premium = ['Sr. dos Aneis', 'Matrix', 'Homem de Ferro', 'Rocco, as aventuras do anel perdido']

    def validar_plano(self):
        if self.plano in self.planos_disponiveis: #Compara o plano do cliente com os planos disponíveis, se não bater, não executa o cadastro
            print(f'Cliente cadastrado!')
        else:
            raise Exception(f'Escolha um destes planos: {self.planos_disponiveis}') #Desta forma é possível subir uma Exception no código
        
    def mudar_plano(self, novo_plano): #recebe o novo plano e valida se está nos planos disponpiveis
        if novo_plano in self.planos_disponiveis:
            self.plano = novo_plano
        else:
            raise Exception('Definição de plano ERRADA')

    def ver_filme(self): #Abre a lista de planos de acordo com o pacote do cliente
        if self.plano in 'basic':
            print(f'{self.nome}, possui estes filmes para hoje:')
            for filme in self.filmes_basic:
                print(filme.upper())
        elif self.plano in 'premium':
            print(f'{self.nome}, possui estes filmes para ver hoje:')
            for filme in self.filmes_premium:
                print(filme.upper())

                
        

#Programa Principal:

c1 = Cliente('gustavo', 'gg@gmail.com', 'basic') #cadastrando cliente
c1.validar_plano() #validando plano
c1.mudar_plano('premium') #Solicitação de mudança de plano
print(f'\nPlano cliente {c1.nome} = {c1.plano}') #Situação do cliente
c2 = Cliente('val', 'valeria@gmail.com', 'basic') #cadastrando cliente
c2.validar_plano() #validando plano
print(f'\nPlano cliente {c2.nome} = {c2.plano}') #Situação do cliente
print(f'\nPara cliente {c1.nome}:')
c1.ver_filme() #Lista dos filmes disponíveis para o plano
print(f'\nPara cliente {c2.nome}:')
c2.ver_filme()
