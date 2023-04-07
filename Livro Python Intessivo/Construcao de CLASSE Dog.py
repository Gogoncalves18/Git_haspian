#https://www.hashtagtreinamentos.com/classes-no-python?gclid=Cj0KCQjwz6ShBhCMARIsAH9A0qWMUJEgtE8M6lx6_kOOR5LZvH7WjqbFNutjw8RLI7C9xV0L-G8A_YAaAgffEALw_wcB
class Dog(): #classe sempre minusculo, nome com a primeira maiuscula. Esta é a classe para definir um objeto como cachorro
    def __init__(self, name, age): #Aqui eu abro a classe Dog dando a ela os atributos (caracteristicas que preciso que ela assuma para compor o objeto)
        self.name = name #vou associando cada atributo recebido para o objeto que o python cria através do self. É como o self criasse um ID para associar as coisas a este ID
        self.age = age
        
def sit(self): #As funções seguintes olharão para o ID que eu crio e que associo a uma variável do programa, assim a variável pertence a um self que gera um ID único para ter um objeto unico
    print(f'{self.name.title()} está sentado!')

def late(self):
    print(f'{self.name.title()} está latindo!')

def rola(self):
    print(f'{self.name.title()} está rolando no chão!')


my_dog = Dog('Haji', 11) #Aponto a variável que aciona a classe para gerar o objeto através dos atributos apontadados, neste caso Haji para nome e 11 para idade
dog2 = Dog('Xinoca', 4)
print(f'Meu cachorro tem o nome de {my_dog.name}') #assim posso chamar atributos da classe
sit(my_dog) #Ou posso apontar funções da classe que executarão ações para aquele objeto
sit(dog2)
late(my_dog)
