from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#O kivy.properties import ObjectProperty carrega propriedades do
#objeto que entra pelo self, um exemplo de como pego o texto do kv
#identifico e trago para a funcao do python

#Exemplo do uso da classe widget que é uma classe completa, por isto 
#que importo dela. Importante lembrar que o nome da classe deve ser
#chamado no KV como <Tela-grade> para o KV vincular as coisas
class Tela_grade(Widget): 
    #Aqui é uma boa pratica sempre limpar a variavel que recebe os 
    #dados do self, colocando NONE dentro do OBJECTPROPERTY
    nome_pessoa = ObjectProperty(None)
    comida_pessoa = ObjectProperty(None)
    cor_pessoa = ObjectProperty(None)

    def apertei(self): #Neste caso não preciso mais usar o termo INSTANCE
        #Aqui repare que eu leio o termo do KV que é a variável NOME que 
        #busca o ID NAME dentro da estrutura do KV e gravo ela em outra variavel
        nome_pessoa = self.nome.text
        comida_pessoa = self.comida.text
        cor_pessoa = self.cor.text

        self.resp = Label(text = f'Meu nome é {nome_pessoa}; Minha comida favorita é {comida_pessoa}; Minha cor é {cor_pessoa}')       
        self.add_widget(self.resp)

        self.nome.text = ''
        self.comida.text = ''
        self.cor.text = ''
      

class Aula_05(App):
    def build(self):
        return Tela_grade()
    
if __name__ == '__main__':
    Aula_05().run()