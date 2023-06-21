#Aula: HashLDash - https://www.youtube.com/watch?v=xdxHJIfgG40&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=2
from kivy.app import App #Importo a classe do aplicativo
from kivy.uix.button import Button #Da classe uix de interfaces eu importo um botao
from kivy.uix.boxlayout import BoxLayout #Constroi telas que empilha widget
from kivy.uix.label import Label

class Test(App): #Herdo da classe app para minha classe teste do app que farei
    def build(self): #chamo a funcao que controi o app
        box = BoxLayout(orientation='vertical') #Chamo a classe boxlayout e instancio ela na variavel box
                        #Dentro de parenteses posso colocar propriedades para mudar orientacao dos widgets
        botao = Button(text='Botao 1') #instancio a classe botaa com texto em botao
        label_tela = Label(text='Texto 1') #Classe para texto
        box.add_widget(botao) #Adiciono o botao no boxlayout instaciado
        box.add_widget(label_tela) #Adiciono o texto no outro widget que dividira tela
        
        box2 = BoxLayout() 
        botao2 = Button(text='Botao 2') 
        label_tela2 = Label(text='Texto 2')
        box2.add_widget(botao2)
        box2.add_widget(label_tela2) 

        box.add_widget(box2)#Adiciono um box layout dentro do outro para formar
        #duas telas na horizontal e duas na vertical dividindo o box em 4 partes

        return box #Construo o box inteiro com tudo dentro
Test().run() #Para rodar o app