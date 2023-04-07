"""NESTE EXEMPLO CRIAREMOS UM CARRO ELETRICO, COMO PARTE DESTE CARRO É IGUAL AO CARRO COMUM,
FAREMOS UMA HERANÇA DE CLASSE PARA NÃO TER QUE CRIAR UMA NOVA CLASSE 
"""
class Car():
    """Representação de tipos e modelos de carro"""
    def __init__(self, maker, model, ano):
        """Inicializando os atributos de cada carro"""
        self.maker = maker
        self.model = model
        self.ano = ano
        self.odom = 0 #Posso iniciar um atributo sem declarar o mesmo na classe

    
    def descr_car(self):
        long_name = str(self.ano)+' '+ self.maker.title() + ' '+ self.model.title()
        return long_name
    
    def odom(self):
        return self.odom
    
    def updt_odom(self, kmage): #self novamente puxa o objeto em questão e este objeto recebe uma variável de KM
        """Define um KM para o odometro que nunca será menor do que o anterior"""
        if kmage <= self.odom: #Função valida a entrada e define se o processo segue
            print(f'Vc não pode inserir um valor menor do que o ODOM atual')
        else: 
            self.odom += kmage #aqui eu atualizo a variavel que foi declarada no objeto na Linha 8 e foi alterada na linha 37


class Eletr_car(Car): #Ao colocar o nome da outra classe chamada "Car", eu assumo os atributos dela nesta nova classe e ainda posso inserir
    #novos atributos
    def __init__(self, maker, model, ano): #esta linha é necessária para assumir os atributos da anterior
        super().__init__(maker, model, ano) #Necessário entrar com o comando Super para que a classe filha herde do pai. Veja que não há ":"
        self.bateria_size = 70 #Aqui defini uma variavel padrão para tamanho da bateria
    
    def descr_bateria(self):
        return f'Este carro eletrico possui bateria {self.bateria_size} KWh.' #Aqui é o metodo que pega o objeto pelo self e puxa o atributo da bateria
    

#CODIGO PRINCIPAL

new_car = Car('audi', 'a4', 2016)
car2 = Car('GM', 'gol', 1993)
print(f'LINHA 43 - {new_car}') #Retorna o ID do objeto
print(f'LINHA 44 - {car2}')
print(f'LINHA 45 - {new_car.descr_car}') #Retorna o metodo apontado para o objeto que será executado
print(f'LINHA 46 - {car2.descr_car}')
print(f'LINHA 47 - {new_car.descr_car()}') #Retorna o metodo escrito dentro da função para descrever o objeto
print(f'LINHA 48 - {car2.descr_car()}')
new_car.odom = 23 #Inputo um valor para o atributo olhando para o objeto New_car
print(f'LINHA 50 - {new_car.odom}') #Aqui acesso o valor do atributo ao qual ele me devolve o valor correto (23) inputado do objeto New_car
print(f'\nLINHA 51 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') # O mesmo comando olhando para o objeto car2 está com o valor zerado ainda
new_car.updt_odom(5) #Desta maneira que eu uso uma função que olha para o objeto e retrabalha ele, PRIMEIRO aponto para o objeto (new_car), depois chamo a função dele para alterá-lo
print(f'\nlINHA 53 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') #mostro o valor do ODOM do objeto antes
new_car.updt_odom(30) #novo dado para linha 8 que entregará a info para o objeto new_car
print(f'\nLINHA 55 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') #mostro o valor do ODOM do objeto depois
car2.updt_odom(200000) #novo dado para linha 8 que entregará a info para o objeto car2
print(f'\nLINHA 57 - O odometro do carro {car2.descr_car()} está com {car2.odom}KM') 
tesla_1 = Eletr_car('tesla', 's', 2023)
print(f'LINHA 59 - {tesla_1.descr_car()}') #Aqui estamos executando um metodo da classe pai, porém dentro da classe filho que herdou os atributos e funções
print(f'LINHA 60 {tesla_1.descr_bateria()}') #maneira de chamar um metodo filho de dentro do pai
