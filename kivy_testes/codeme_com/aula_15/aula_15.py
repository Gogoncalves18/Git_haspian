from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('aula_15.kv')

class Box(Widget): 
    #Criado esta funcao para limpar a tela forçando a entrada do zero
    def clear(self):
        #Este ID é do TEXTINPUT
        self.ids.tela_res.text = '0'

    #Nesta funcao eu recebo os botoes numericos que estou pressionando
    #assim saberei qual o vlr estou apertando, recebo ele no VLR_BTN
    def btn_act(self, vlr_btn):
        #Gravo o vlr da tela TEXTINPUT em uma variavel
        new_num = self.ids.tela_res.text

        #Condicional para saber que se a tela está em zero, eu devol limpar
        #ela
        if new_num == "0":
            self.ids.tela_res.text = ''
            self.ids.tela_res.text = f'{vlr_btn}'
        else:
            #Quando nao é zero, ai apenas pego um numero, junto com o novo 
            #e volto a guardar o valor na variavel no proximo acionamento
            self.ids.tela_res.text = f'{new_num}{vlr_btn}'

    def add(self):
        self.ids.tela_res.text = f'{self.ids.tela_res.text}+'

    def div(self):
        self.ids.tela_res.text = f'{self.ids.tela_res.text}/'

    def minus(self):
        self.ids.tela_res.text = f'{self.ids.tela_res.text}-' 

    def mult(self):
        self.ids.tela_res.text = f'{self.ids.tela_res.text}*'      

    def btn_res(self):
        #Registrar o valor digitado na tela em str()
        res_dig = self.ids.tela_res.text
        if '+' in res_dig:
            #Monto uma lista separando pelo sinal '+'
            list_vlr_res_dig = res_dig.split('+')
            #Variavel para guardar valor da operaco de soma
            res_op = 0 
            for n in list_vlr_res_dig:
                res_op += int(n)
            self.ids.tela_res.text = ''
            #Preciso transformar em str() novamente pq o Label só lê isto
            self.ids.tela_res.text = str(res_op)

class Minha_calc(App): 
    def build(self):
        Window.size = [300,520] 
        Window.clearcolor = (0.4,0,0.2,1)
        return Box()
    
if __name__ == '__main__':
    Minha_calc().run()