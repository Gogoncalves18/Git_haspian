from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('aula_07.kv')

class Tela_grade(Widget): 
    nome_pessoa = ObjectProperty(None)
    comida_pessoa = ObjectProperty(None)
    cor_pessoa = ObjectProperty(None)

    def apertei(self): 
        nome_pessoa = self.nome.text
        comida_pessoa = self.comida.text
        cor_pessoa = self.cor.text

        self.nome.text = ''
        self.comida.text = ''
        self.cor.text = ''
      

class Meu_app(App): 
    def build(self):
        return Tela_grade()
    
if __name__ == '__main__':
    Meu_app().run()