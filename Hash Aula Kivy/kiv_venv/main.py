#Aula: HashLDash - https://www.youtube.com/watch?v=xdxHJIfgG40&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=2
from kivy.app import App #Importo a classe do aplicativo
from kivy.uix.boxlayout import BoxLayout #Constroi telas que empilha widget

class incrementador(BoxLayout): #herdo da classe boxlayout funcoes para o incrementador
    pass

class Test(App): #Herdo da classe app para minha classe teste do app que farei
    def build(self): #chamo a funcao que controi o app
        return incrementador() #Construo o box inteiro com tudo dentro
    
    
Test().run() #Para rodar o app