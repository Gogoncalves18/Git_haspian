from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
#Definicao de tamanho de janela
from kivy.core.window import Window
#Local para tratar imagem no kivy
from kivy.uix.image import Image

Builder.load_file('aula_12.kv')

class Box(Widget): 
    pass      

class Meu_app(App): 
    def build(self):
        Window.size = [300,560] #Precisa ser uma lista de valores
        #Neste caso eu consigo colocar uma cor no background
        #da janela ao inves de usar um canvas no KV bem
        #no inicio da primeira classe
        Window.clearcolor = (0,.5,0.5,1)
        return Box()
    
if __name__ == '__main__':
    Meu_app().run()