from kivy.app import App #Importo a classe do aplicativo
from kivy.uix.button import Button #Da classe uix de interfaces eu importo um botao

class Test(App): #Herdo da classe app para minha classe teste do app que farei
    def build(self): #chamo a funcao que controi o app
        return Button(text='Ola Mundo') #retorno dela a classe botao para construir o botao e posso inputar texto dentro dele
    
Test().run() #Para rodar o appcla