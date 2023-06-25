# AULA - https://youtu.be/WmiKgFBIqkE
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class Tarefas(ScrollView): #Criacao de tarefas na tela, adicionei o scroll para ter rolagem na tela, ela ficará dentro do 
    #boxlayout definido no .kv
    def __init__(self, tarefas, **kwargs): #funcao para receber infos 'tarefas' que sera uma lista
        #os **kwargs é para receber parametros extras 
        super().__init__(**kwargs) #preciso herdar o init senao ele sobrescrevera  init do boxlayout
        for tarefa in tarefas: #Rodo a lista que recebo
            self.ids.box.add_widget(Tarefa(text = tarefa)) #Uso o boxlayout para inserir os
            #widgets no layout. Neste caso, o 'ids' define que chamarei um widget do .kv e o 'box' é o widget
            #ao qual vou adicionar o widget atraves da funcao tarefa. Dentro do da funcao entregarei o texto tarefa do loop

class Tarefa(BoxLayout): # Esta funcao eu preciso configurar no .kv como <Tarefa>
    def __init__(self, text = '', **kwargs): #Inicializo a funçao e dou um text vazio para ela receber o texto do "box.add_widget"
        super().__init__(**kwargs)
        self.ids.label_task.text = text # Aqui pego o texto enviado pela funcao Tarefas e insiro um a um
                                        #em label_task no .kv  

class AppMain(App):
    def build(self):
        Window.size = [300,560] #Travo o tamanho da tela para parece um celular
        return Tarefas(['cafe', 'futebol', 'almoco', 'filme', 'namorar', 'pipoca', 'carinho dog', 'beijinho na nega', 'cheirinho', 'mais beijinho']) 
            #Aqui estou passando um parametro extra para entregar para a classe Tarefas que #kwargs
            #Podemos ver que ele sobrescrevera o .KV
    
AppMain().run()