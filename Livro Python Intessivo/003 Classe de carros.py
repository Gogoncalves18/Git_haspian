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

    

#CODIGO PRINCIPAL

new_car = Car('audi', 'a4', 2016)
car2 = Car('GM', 'gol', 1993)
print(f'LINHA 31 - {new_car}') #Retorna o ID do objeto
print(f'LINHA 32 - {car2}')
print(f'LINHA 33 - {new_car.descr_car}') #Retorna o metodo apontado para o objeto que será executado
print(f'LINHA 34 - {car2.descr_car}')
print(f'LINHA 35 - {new_car.descr_car()}') #Retorna o metodo escrito dentro da função para descrever o objeto
print(f'LINHA 36 - {car2.descr_car()}')
new_car.odom = 23 #Inputo um valor para o atributo olhando para o objeto New_car
print(f'LINHA 38 - {new_car.odom}') #Aqui acesso o valor do atributo ao qual ele me devolve o valor correto (23) inputado do objeto New_car
print(f'\nLINHA 39 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') # O mesmo comando olhando para o objeto car2 está com o valor zerado ainda
new_car.updt_odom(5) #Desta maneira que eu uso uma função que olha para o objeto e retrabalha ele, PRIMEIRO aponto para o objeto (new_car), depois chamo a função dele para alterá-lo
print(f'\nlINHA 41 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') #mostro o valor do ODOM do objeto antes
new_car.updt_odom(30) #novo dado para linha 8 que entregará a info para o objeto new_car
print(f'\nLINHA 43 - O odometro do carro {new_car.descr_car()} está com {new_car.odom}KM') #mostro o valor do ODOM do objeto depois
car2.updt_odom(200000) #novo dado para linha 8 que entregará a info para o objeto car2
print(f'\nLINHA 45 - O odometro do carro {car2.descr_car()} está com {car2.odom}KM') 
