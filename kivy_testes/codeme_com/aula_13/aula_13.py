from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
#importacao do floatlayout que ancora os widget por posicao na tela
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('aula_13.kv')

class Box(Widget): 
    pass      

class Meu_app(App): 
    def build(self):
        Window.size = [400,600] 
        Window.clearcolor = (0.4,0,0.2,1)
        return Box()
    
if __name__ == '__main__':
    Meu_app().run()