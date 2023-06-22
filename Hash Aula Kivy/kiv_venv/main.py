#Aula: HashLDash - https://www.youtube.com/watch?v=xdxHJIfgG40&list=PLsMpSZTgkF5AV1FmALMgW8W-TvrfR3nrs&index=2
from kivy.app import App #Importo a classe do aplicativo
from kivy.uix.button import Button #Da classe uix de interfaces eu importo um botao
from kivy.uix.boxlayout import BoxLayout #Constroi telas que empilha widget
from kivy.uix.label import Label

class Test(App): #Herdo da classe app para minha classe teste do app que farei
    def build(self): #chamo a funcao que controi o app
        box = BoxLayout(orientation='vertical') #Chamo a classe boxlayout e instancio ela na variavel box
                        #Dentro de parenteses posso colocar propriedades para mudar orientacao dos widgets
        botao = Button(text='Botao 1',
                       font_size=30,
                       on_release=self.incrementar,
                       ) 
                        #instancio a classe botaa com texto em botao
                        #Pode receber tamanho da fonte
                        #On_release ou on_press são eventos que quando acontence na classe Button, posso acionar uma funcao ao qual devo chamar como self.nome_da_funcao
        self.label_tela = Label(text='1') #Classe para texto
            #Adiciono o self. no label para instanciar ele como uma variavel unica dentro da classe Test, assim posso acessar ele de qualquer lugar dentro da classe
        box.add_widget(botao) #Adiciono o botao no boxlayout instaciado
        box.add_widget(self.label_tela) #Adiciono o texto no outro widget que dividira tela
    
        return box #Construo o box inteiro com tudo dentro
    
    def incrementar(self, botao): #Aqui devo montar o padrao da funcao e depois chamar a variavel que instanciei a classe Button
        botao.text='Soltei' #Com a variavel instaciada, posso alterar a propriedade texto dentro dela
        self.label_tela.text = str(int(self.label_tela.text)+1)
            #chamo a variavel label atraves do self. da classe e a propriedade dele .text, transformo ele em numero para somar e depois em texto para colocar dentro do label

Test().run() #Para rodar o app