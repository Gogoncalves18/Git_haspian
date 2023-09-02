from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('aula_17.kv')

class Box(Widget): 
    #Criado esta funcao para limpar a tela forçando a entrada do zero
    def clear(self):
        #Este ID é do TEXTINPUT
        self.ids.tela_res.text = '0'

    def remover(self):
        #Remove um item da STR
        new_input = self.ids.tela_res.text
        #Retiro o ultimo item do STR
        new_input = new_input[:-1]
        self.ids.tela_res.text = new_input

    def troca_sinal(self):
        new_input = self.ids.tela_res.text
        if new_input == '0':
            #Coloco o sinal - se o valor for ZERO
            self.ids.tela_res.text = ''
            new_input = self.ids.tela_res.text
            #Neste caso uso o REPLACE ao qual a primeira posicao de "" é 
            #para colocar o sinal de - e a segunda posicao de "" diz onde
            #colocar o sinal de -. Neste caso com a segunda posicao esta vazia
            #Ela entra sempre na posicao que não há ocupacao de caracter
            self.ids.tela_res.text = f'{new_input.replace("-", "")}'
        else:
            self.ids.tela_res.text = f'-{new_input}'
        

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
           #Condicao para adicionar o '.' para transformar em float, lembrando
           # que o label não aceita INT ou FLOAT, somente STR 
        elif vlr_btn == '.':
            if '.' in new_num:
                pass
            else:
                self.ids.tela_res.text = f'{self.ids.tela_res.text}.'
        else:
            #Quando nao é zero, ai apenas pego um numero, junto com o novo 
            #e volto a guardar o valor na variavel no proximo acionamento
            self.ids.tela_res.text = f'{new_num}{vlr_btn}'

    def sinal_op(self, operador):
        self.ids.tela_res.text = f'{self.ids.tela_res.text}{operador}'

    def btn_res(self):
        #Registrar o valor digitado na tela em str()
        res_dig = self.ids.tela_res.text
        if '+' in res_dig:
            #Monto uma lista separando pelo sinal '+'
            list_vlr_res_dig = res_dig.split('+')
            #Variavel para guardar valor da operaco de soma
            res_op = 0 
            for n in list_vlr_res_dig:
                #Condicao para fazer a operacao quando o dado é float
                #ou int, para nao dar erro na operacao
                if '.' in n:
                    res_op += float(n)
                else:
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