from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

#Pagina 88 da documentacao kivy

class Widget_Root(BoxLayout): #Herdo de box layout
    def __init__(self, **kwargs):
        super(Widget_Root, self).__init__(**kwargs)
        self.add_widget(Button(text='Btn_1', **kwargs)) # Adiciono o botao do kivy
        cd = CustomBtn() # Chamo uma classe especial e instancio ela
        cd.bind(pressed=self.btn_pressed)
        self.add_widget(cd)
        self.add_widget(Button(text='Btn_2')) # Adiciono outro botao

    def btn_pressed(self, instance, pos):
        print(f'Valor recebido na funcao BTN_Pressed = {instance}')
        print(f'printado posicao da funcao btn do widget root {pos}')

class CustomBtn(Widget): # Classe especial herdade de widget
    pressed = ListProperty([0,0]) # Crio uma varial global que será lida pelo bind do cd.bind
    
    def on_touch_down(self, touch): 
        print(f'Posicao original: {self.pressed}') # Aqui o primeiro clique mostrar a pos 0,0, mas o segundo cliente mostra a ultima info gravada
        if self.collide_point(*touch.pos): #Aqui é usado *touch para manter as otras infos empacotadas e entao posso chamar o .pos para ler o atributo pos
            print(f'Dados Touch = {touch}') # Aqui o touch descarrega tudo que há dentro de <MouseMotionEvent
            self.pressed = touch.pos
            return True # Para parar a funcao
        return super(CustomBtn, self).on_touch_down(touch) # Linha padrao do on_touch_down
    
    def on_touch_move(self, touch):
        print(f'Infos do move: {touch}')
        return super().on_touch_move(touch)

    def on_pressed(self, instance, pos): #Aqui para mostrar que esta funcao também traz a mesma info
        print(f'Pressionado na posicao {pos}')
        print(f'O que recebo em on_pressed = {instance}')

class TestApp(App):
    def build(self):
        return Widget_Root()
    
if __name__=='__main__':
    TestApp().run()