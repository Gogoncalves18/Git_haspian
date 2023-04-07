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
    

#CODIGO PRINCIPAL

new_car = Car('audi', 'a4', 2016)
car2 = Car('GM', 'gol', 1993)
print(new_car) #Retorna o ID do objeto
print(car2)
print(new_car.descr_car) #Retorna o metodo apontado para o objeto que será executado
print(car2.descr_car)
print(new_car.descr_car()) #Retorna o metodo escrito dentro da função para descrever o objeto
print(car2.descr_car())
new_car.odom = 23
print(new_car.odom)
print(car2.odom)
