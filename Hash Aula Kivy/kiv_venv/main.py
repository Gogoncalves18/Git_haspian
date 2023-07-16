# AULA - https://youtu.be/WmiKgFBIqkE
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen #Preciso importar ambos,
        #um é o gerenciador e o outro é a tela
from kivy.uix.behaviors.button import ButtonBehavior # Para desenhar botao Person2
from kivy.uix.label import Label # Para desenhar botao Person2
from kivy.graphics import Ellipse, Rectangle, Color # Para desenhar botao Person2


class GerenciadorTela(ScreenManager):
    pass

class Menu(Screen):
    pass

class BotaoPerson2(Label, ButtonBehavior): #Herdo classes igual .kv
    def __init__(self, **kwargs): # Preciso iniciar a classe para produzir botao
        super(BotaoPerson2, self).__init__(**kwargs) # Preciso rodar o super para nao
            #sobre escrever a classe de label e buttonbehavior
        self.atualizar() # Chamo a atualizacao

        # Ate aqui o novo botao nao sai na posicao certa, por isto precisaremos redesenhar
        #ele antes de chamar, como uma funcao de 'atualizar' posicao e tamanho

    def on_pos(self, *args): # Funcao do kivy que é disparada sempre alguma posicao muda
        self.atualizar()

    def on_size(self, *args): # Funcao do kivy que é disparada sempre algum tamanho muda
        self.atualizar()

    def atualizar(self, *args): # Criado funcao para atualizar a todo momento
        self.canvas.before.clear() # Para apagar rastros do redesenho o canvas    
        with self.canvas.before: # A maneira de buscar o funcao canvas é com 'With'
            Color(rgba=(0.28,0.4,0.69,1))
            Ellipse(size=(self.height, self.height),
                    pos=(self.pos))
            Ellipse(size=(self.height, self.height),
                    pos=(self.x + self.width - self.height, self.y))
            Rectangle(size=(self.width - self.height, self.height),
                      pos=(self.x + (self.height/2.0), self.y)) #aqui temos que usar
                        #2.0 pq no python2 que o kivy usa, 1/2 ele devolve 0

    def on_touch_down(self, touch):
        if self.collide_point(*touch):
            self.on_release
        return super().on_touch_down(touch)
        
class Tarefas(Screen): # Neste caso deixo de usar o boxlayout e uso o Screen para se
    #gerenciado pelo ScreenManager com um tela
    def __init__(self, tarefas = [], **kwargs): #funcao para receber infos 'tarefas' que sera uma lista
        #os **kwargs é para receber parametros extras 
        super().__init__(**kwargs) #preciso herdar o init senao ele sobrescrevera  init do boxlayout
        for tarefa in tarefas: #Rodo a lista que recebo
            self.ids.box.add_widget(Tarefa(text = tarefa)) #Uso o boxlayout para inserir os
            #widgets no layout. Neste caso, o 'ids' define que chamarei um widget do .kv e o 'box' é o widget
            #ao qual vou adicionar o widget atraves da funcao tarefa. Dentro do da funcao entregarei o texto tarefa do loop

    def on_pre_enter(self): # É uma funcao do Kivy que devolve os eventos de teclado
        Window.bind(on_keyboard = self.voltar) # Aqui o bind ESTA vinculando os eventos
                    #de teclado que acontece quando estou dentro da tela 'Tarefas'.
                    # O 'on_keyboard' está pegando este eventos. Sendo assim, toda vez
                    #que uma tecla for usada, eu vou chamar a funcao 'self.voltar'

    def voltar(self, window, key, *args): # Aqui eu vou receber infos do módulo tela. Se eu nao
                #usar o window, quando solicitar para ler a tecla, ele vai me devolver
                #somente o objeto da sld2 que é a janela.
                #e o 'on_keyboard' me entrega: key, scancode, codepoint, modifier. Como
                #vou usar apenas o 'key', o resto entrego para o *args
        #print(key)
        if key == 27:
            #print(App.get_running_app().root) # Aqui posso ver que o 'App.get_running_app
                    #chama o nome de quem é a funcao e onde estou, quando coloco '.root'
                    #recebo o nome do 'GerenciadorTela'
            App.get_running_app().root.current = 'menu' # Aqui chamo a tela de menu
            return True # Executar o 'return' em uma funcao é a mesma coisa que definir
                #que capturamos a info e nao queremos passar ela adiante, para outros
                #eventos, ela para apos isto.

    def on_pre_leave(self, *args): # O kivy executará esta funcao sempre que for solicitado
        #a deixar a tela de tarefas
        Window.unbind(on_keyboard = self.voltar) # Como o bind vinculoy ao modulo window tudo
            #que estava acontecendo com os eventos de teclado dentro de tarefa, precisamos 
            #executar um '.unbind()' para que a tecla ESC (27) volte a funcionar quando nao
            #estou dentro da tela tarefas
    
    def addinfo(self):
        texto = self.ids.text_in.text # Gravo na variavel texto os dados inserido
                #em "ids.text_in" com o self pois assim pego o objeto. O ".text" é 
                #uma propriedade do "TextInput" para pegar o texto
        self.ids.box.add_widget(Tarefa(text = texto)) # Aqui chamo o "ids.box" e uso
                # a funcao "add_widget" do Boxlayout, assim passo a classe "Tarefa" 
                # apontando a variavel "texto" onde gravei o dado digitado
        self.ids.text_in.text = '' # Insiro na sequencia um texto vazio em "ids.text_in"
                #para quando adicionar o texto principal, a janela fica vazia
    

class Tarefa(BoxLayout): # Esta funcao eu preciso configurar no .kv como <Tarefa>
    def __init__(self, text = '', **kwargs): #Inicializo a funçao e dou um text vazio para ela receber o texto do "box.add_widget"
        super().__init__(**kwargs)
        self.ids.label_task.text = text # Aqui pego o texto enviado pela funcao Tarefas e insiro um a um
                                        #em label_task no .kv  

class AppMain(App):
    def build(self):
        Window.size = [300,560] #Travo o tamanho da tela para parece um celular
        return GerenciadorTela() #Deixei de usara a classe Tarefas e passo a carregar
                #no construtor o Gerenciador de telas
    
AppMain().run()

'''No Kivy há eventos que ele lê conforme as coisas vao acontecendo, nao somente
quando acontece mas tambem em momentos antes, vide exemplo:
on_enter, on_leave, on_pre_enter, on_pre_leave
'''

#Tarefas(['cafe', 'futebol', 'almoco', 'filme', 'namorar', 'pipoca', 'carinho dog', 'beijinho na nega', 'cheirinho', 'mais beijinho']) 
            #Aqui estou passando um parametro extra para entregar para a classe Tarefas que #kwargs
            #Podemos ver que ele sobrescrevera o .KV