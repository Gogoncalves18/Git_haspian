from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('aula_22.kv')

class Box(Widget): 
   pass

class kivyApp(App): 
    def build(self):
        Window.size = [400,680] 
        Window.clearcolor = (1,1,1,1)
        return Box()
    
if __name__ == '__main__':
    kivyApp().run()