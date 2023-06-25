#Aula: HashLDash - https://www.youtube.com/watch?v=xdxHJIfgG40&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=2
from kivy.uix.boxlayout import BoxLayout #Constroi telas que empilha widget
from kivy.uix.label import Label

class Tarefas(BoxLayout): #herdo da classe boxlayout funcoes para o incrementador
    BoxLayout.add_widget.Label(text = 'tarefa')    
        