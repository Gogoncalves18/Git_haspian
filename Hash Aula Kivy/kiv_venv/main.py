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
            self.ids.box.add_widget(Label(text = tarefa, font_size = 20, size_hint_y = None, height = 80)) #Uso o box layout para inserir os
            #widgets no layout. Neste caso, o 'ids' define que chamarei um widget do .kv e o 'box' é o widget
            #ao qual vou adicionar o widget 'label'. Dentro do label se não desligar o 'size_hint', os widgets ficará um em cima do outro.
            # Como desliguei o hint do boxlayout no .kv, é necessário desligarmos aqui no label e determinar uma altura, aqui de 200 pixel.            

class AppMain(App):
    def build(self):
        Window.size = [300,560] #Travo o tamanho da tela para parece um celular
        return Tarefas(['cafe', 'futebol', 'almoco', 'filme', 'namorar', 'pipoca', 'carinho dog', 'beijinho na nega', 'cheirinho', 'mais beijinho']) 
            #Aqui estou passando um parametro extra para entregar para a classe Tarefas que #kwargs
            #Podemos ver que ele sobrescrevera o .KV
    
AppMain().run()