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
        self.bateria = Battery() #Aqui eu puxei para o atributo desta classe de carro a saída da classe de bateria. Uma classe alimentando um atributo
    
    def descr_bateria(self):
        return f'Este carro eletrico possui bateria {self.bateria_size} KWh.' #Aqui é o metodo que pega o objeto pelo self e puxa o atributo da bateria


class Battery(): #Definimos uma nova classe só para bateria para detalhar melhor ela e associa-la aos atributos das outras classes
    """Modelamento das caracteristicas de bateria"""
    def __init__(self, bateria_size=70):
        self.bateria_size = bateria_size

    def descr_bat(self):
        """Exibe uma decrição completa da bateria"""
        return f'Este carro possui uma bateria de {self.bateria_size}-KWh.'