from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#A importacao abaixo é para definir o nome do meu kv sem me 
#preocupar com o nome da CLASS MEU_APP que deve ser igual ao 
#nome KV
from kivy.lang import Builder

Builder.load_file('aula_06.kv') #Defino qual kv ele deve ler

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
      

class Meu_app(App): #Com a linha 09, posso usar qq nome no meu APP
    def build(self):
        return Tela_grade()
    
if __name__ == '__main__':
    Meu_app().run()