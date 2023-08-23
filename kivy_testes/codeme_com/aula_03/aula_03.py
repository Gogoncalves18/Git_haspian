from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

'''Importacao do label é para colocar titulo texto 
    Gridlayout traz uma especie de tabela 
    TextInput para entrada de texto pelo user
    Button para criar botao
'''
#Crio minha classe que será meu root para chamar no contrutor do Myapp(App)
class Meu_grid(GridLayout): 
    def __init__(self, **kwargs):
        #Apos inicializar o construtor eu passo a heranca para minha classe
        super(Meu_grid, self).__init__(**kwargs)
        
        #Aqui defino criacao do grid com uma coluna que comportará
        #primeiro o grid com duas colunas e depois virá o resto
        #grid com uma coluna com o botao de SELF.SUBMETER e o SELF.RESP
        self.cols = 1

        #Dentro do grid de uma coluna instancio um outro grid que será inserido
        #Importante entender que o kivy desenhará o espaço com 1 coluna, entao 
        #encontrará o espaço com duas colunas, receberá as instruções de ADD_WIDGET
        #e então voltará para o esaço de uma coluna com SELF.SUBMETER e o SELF.RESP
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        #adiciono na coluna 1 um label com identificacao do campo como nome
        self.top_grid.add_widget(Label (text = 'Name: '))

        #NEste caso adiciono um campo de entrada de texto pelo 
        #TextInput, nele uso o parametro para definir se quero
        #que ele tenha multiplas linhas ou apenas uma linha infinita
        #E instancio este texto na propriedade name
        self.name = TextInput(multiline = True)
        #Apos devo chamar a entrada de texto para dentro de ADD_WIDGET, passando
        #para ele o texto instanciado
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label (text = 'Food: '))

        self.food = TextInput(multiline = True)
        self.top_grid.add_widget(self.food)

        self.top_grid.add_widget(Label (text = 'Cor: '))

        self.cor = TextInput(multiline = True)
        self.top_grid.add_widget(self.cor)

        #Aqui que eu adiciono toda a construção do grid de 2 colunas
        self.add_widget(self.top_grid)

        #Aqui posso instanciar o botao desta forma abaixo ou simplificar a linha
        #de comando para deixar o codigo mais claro como a partir da linha 45
        #self.add_widget(Button(text = 'Submeter'))

        self.submeter = Button(text = 'Submeter', font_size = '40dp')

        #Neste caso uso a funcao BIND do kivy para ficar escutando o botao
        #ao qual quando ele escuta que que precionei o botao atraves da 
        #funcao padrao do kivy de ON_PRESS, ele aciona a minha funcao APERTEI
        self.submeter.bind(on_press = self.apertei)

        #Aqui adiciono a adicao do widget a instancia de botao criada
        self.add_widget(self.submeter)

    #Aqui a execucao da funcao atraves do evento acima, ela passa para a funcao
    #o objeto a a instancia de dados
    def apertei(self, instance):
        #No caso abaixo estou instanciando os textos adicionados no objeto acima
        #para NAME, FOOD E COR
        name = self.name.text
        food = self.food.text
        cor = self.cor.text

        #Aqui eu adiciono o LABEL no GRID que ficará ao lado da botao 
        #E então aciono o LABEL ao lado do botao com os textos fornecidos 
        #pelas propriedades
        self.resp = Label(text = f'Meu nome é {name}; Minha comida favorita é {food}; Minha cor é {cor}')       
        self.add_widget(self.resp)

        #A maneira abaixo é para limpar os campos quando submeto o clique no botao
        self.name.text = ''
        self.food.text = ''
        self.cor.text = ''

        # print(f'>>>>>>>>> Meu nome é {name};'
        #       f'\nMinha comida favorita é {food};'
        #       f'\nMinha cor é {cor} <<<<<<<<;'
        #       )


class Myapp(App):
    def build(self):
        return Meu_grid() #Nao posso esquecer de chamar minha funcao 
    
if __name__ == '__main__':
    Myapp().run()