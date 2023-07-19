from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Ellipse, Rectangle, Color
from kivy.config import Config 
      
Config.set('graphics', 'resizable', False)

class tela_manag(BoxLayout):
    pass

class btn(ButtonBehavior, Label): # classe para construir um botao ao qual uso apenas 
                    #o a classe ButtonBehavior para assumir comportamentos apenas e 
                    #a classe label, assim posso trabalhar o .kv com estes recursos
    def __init__(self, **kwargs):
        super(btn, self).__init__(**kwargs)
        self.atualizar() # Chamo a funcao para atualizar/desenhar o btn sempre que a classe é construida

    def on_pos(self, *args): # Funcao do kivy que é disparada sempre alguma posicao muda
        self.atualizar() # Redesenho o btn, para acertar posicao

    def on_size(self, *args): # Funcao do kivy que é disparada sempre algum tamanho muda
        self.atualizar() # Redesenho o btn, para acertar posicao

    def atualizar(self, *args, **kwargs): # Criado funcao para desenhar o btn
        self.canvas.before.clear() # Para apagar rastros do redesenho do canvas em mseg que acontece   
        with self.canvas.before: # A maneira de buscar o funcao canvas é com 'With' e o uso do before é para ele ser 
                        #desenhado antes de qq coisa para ficar por baixo do label que usei no .kv
            Color(rgba=(0.28,0.4,0.69,1))
            # Os self abaixo são para assumir o tamanho que o próprio boxlayout reserva para ele no .kv, assim
            #fica mais facil posicionarmos e ajustarmos o tamanho
            Ellipse(
                    size=(50, 50),
                    pos=(self.x+50, self.center_y-25)                 
                    )
            Ellipse(
                    size=(50, 50),
                    pos=(self.width-75, self.center_y-25)
                    )
            Rectangle(
                size=(self.width-125,50),
                pos=(self.x+75, self.center_y-25)
                      )               
    def on_touch_down(self, touch): # Esta é uma funcao reservada do kivy, ele pega todos os eventos de toque na tela 
        #toda. Usei ela pq não consegui usar o on_press somente dentro do desenho do canvas. O touch como atributo me
        #entrega dois atributos em lista, spos e pos, dentro deles eu tenho o x e y do toque. Usei a condição abaixo 
        #para prosseguir somente se o toque for dentro do tamanho do canvas desenhado, dentro de suas coordenadas x,y
        if touch.pos[0] >50 and touch.pos[0] < self.width-75:
            if touch.pos[1] > self.center_y-25 and touch.pos[1] < self.center_y+25:
                print(touch.pos[0]) 
 
class AppM(App):
    def build(self):
        Window.size = [300,560]
        return tela_manag()
    
AppM().run()