from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
#Definicao de tamanho de janela
from kivy.core.window import Window

Builder.load_file('aula_08.kv')

class Box(Widget): 
    pass      

class Meu_app(App): 
    def build(self):
        Window.size = [300,560] #Precisa ser uma lista de valores
        return Box()
    
if __name__ == '__main__':
    Meu_app().run()