from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
#importacao do floatlayout que ancora os widget por posicao na tela
from kivy.uix.floatlayout import FloatLayout

Builder.load_file('aula_14.kv')

class Box(Widget): 
    def aceitar(self):
        #Para instaciar o ID do KV dentro do python, eu preciso
        #buscar por SELF para receber a instancia, por IDS para 
        #ele varrer todos IDS que tem dentro do KV e por .CAMPO 
        #que quero ler, neste caso .TEXT do TEXTINPUT
        frase = self.ids.resp_input.text 
        #print(f'>>>>>>>>>{frase}')     

        #Para fazer aparecer no LABEL a frase, é só carregar a 
        #variavel que gravei FRASE no endereço do text do LABEL
        self.ids.frase_label.text = f'Olá meu amigo {frase}!'
        #Aqui eu só limpo o campo do TEXTINPUT
        self.ids.resp_input.text = ''

class Meu_app(App): 
    def build(self):
        Window.size = [300,520] 
        Window.clearcolor = (0.4,0,0.2,1)
        return Box()
    
if __name__ == '__main__':
    Meu_app().run()