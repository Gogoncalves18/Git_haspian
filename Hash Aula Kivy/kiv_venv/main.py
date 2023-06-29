# AULA - https://youtu.be/WmiKgFBIqkE
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen #Preciso importar ambos,
        #um é o gerenciador e o outro é a tela

class GerenciadorTela(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen): # Neste caso deixo de usar o boxlayout e uso o Screen para se
    #gerenciado pelo ScreenManager com um tela
    def __init__(self, tarefas = [], **kwargs): #funcao para receber infos 'tarefas' que sera uma lista
        #os **kwargs é para receber parametros extras 
        super().__init__(**kwargs) #preciso herdar o init senao ele sobrescrevera  init do boxlayout
        for tarefa in tarefas: #Rodo a lista que recebo
            self.ids.box.add_widget(Tarefa(text = tarefa)) #Uso o boxlayout para inserir os
            #widgets no layout. Neste caso, o 'ids' define que chamarei um widget do .kv e o 'box' é o widget
            #ao qual vou adicionar o widget atraves da funcao tarefa. Dentro do da funcao entregarei o texto tarefa do loop

    def addinfo(self):
        texto = self.ids.text_in.text # Gravo na variavel texto os dados inserido
                #em "ids.text_in" com o self pois assim pego o objeto. O ".text" é 
                #uma propriedade do "TextInput" para pegar o texto
        self.ids.box.add_widget(Tarefa(text = texto)) # Aqui chamo o "ids.box" e uso
                # a funcao "add_widget" do Boxlayout, assim passo a classe "Tarefa" 
                # apontando a variavel "texto" onde gravei o dado digitado
        self.ids.text_in.text = '' # Insiro na sequencia um texto vazio em "ids.text_in"
                #para quando adicionar o texto principal, a janela fica vazia
    

class Tarefa(BoxLayout): # Esta funcao eu preciso configurar no .kv como <Tarefa>
    def __init__(self, text = '', **kwargs): #Inicializo a funçao e dou um text vazio para ela receber o texto do "box.add_widget"
        super().__init__(**kwargs)
        self.ids.label_task.text = text # Aqui pego o texto enviado pela funcao Tarefas e insiro um a um
                                        #em label_task no .kv  

class AppMain(App):
    def build(self):
        Window.size = [300,560] #Travo o tamanho da tela para parece um celular
        return GerenciadorTela() #Deixei de usara a classe Tarefas e passo a carregar
                #no construtor o Gerenciador de telas
    
AppMain().run()

#Tarefas(['cafe', 'futebol', 'almoco', 'filme', 'namorar', 'pipoca', 'carinho dog', 'beijinho na nega', 'cheirinho', 'mais beijinho']) 
            #Aqui estou passando um parametro extra para entregar para a classe Tarefas que #kwargs
            #Podemos ver que ele sobrescrevera o .KV