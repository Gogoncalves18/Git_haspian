from kivy.app import App
from kivy.uix.label import Label


class Myapp(App):
    def build(self):
        return Label(text = 'Hello world', font_size = '200dp')
    
if __name__ == '__main__':
    Myapp().run()
