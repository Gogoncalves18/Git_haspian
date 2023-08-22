# AULA - https://youtu.be/WmiKgFBIqkE
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen #Preciso importar ambos,
        #um é o gerenciador e o outro é a tela
from kivy.uix.behaviors.button import ButtonBehavior # Para desenhar botao Person2
from kivy.uix.label import Label # Para desenhar botao Person2
from kivy.graphics import Ellipse, Rectangle, Color # Para desenhar botao Person2
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from kivy.uix.image import Image


class GerenciadorTela(ScreenManager):
    pass

class Menu(Screen):
    def confirmacao(self, *args):
        box = BoxLayout(orientation = 'vertical',
                        padding = 0,
                        spacing = 5,
                        )
                        # size_hint = (None, None),
                        # size = (300, 150),

        btns = BoxLayout(orientation = 'vertical',
                        padding = 0,
                        spacing = 5,                        
                        )
        # size_hint = (None, None),
        #                 size = (self.width-30, 60),

        sim = BotaoPerson2(text = 'SIM')
        nao = BotaoPerson2(text = 'NÃO')

        btns.add_widget(sim)
        btns.add_widget(nao)

        atencao = Image(source = 'img_atencao.png')

        box.add_widget(atencao)
        box.add_widget(btns)

        pop = Popup(title = 'Deseja mesmo sair?', 
                    content = box, 
                    size_hint = (None, None),
                    size = (self.width, self.height/3),                                        
                    )
        pop.open()

class BotaoPerson2(ButtonBehavior, Label): # classe para construir um botao ao qual uso apenas 
                    #o a classe ButtonBehavior para assumir comportamentos apenas e 
                    #a classe label, assim posso trabalhar o .kv com estes recursos
    cor = ListProperty([0.28,0.4,0.69,1])
            #crio uma cor definida atraves do atributo de cor que é uma propriedade 
            #armazenada em uma listproperty que preciso importar no kivy
    cor_pressed = ListProperty([0.1,0.1,0.1,1])

    def __init__(self, **kwargs):
        super(BotaoPerson2, self).__init__(**kwargs)
        self.atualizar_btn_person() # Chamo a funcao para atualizar_btn_person/desenhar o btn sempre que a classe é construida

    def on_pos(self, *args): # Funcao do kivy que é disparada sempre alguma posicao muda
        self.atualizar_btn_person() # Redesenho o btn, para acertar posicao

    def on_size(self, *args): # Funcao do kivy que é disparada sempre algum tamanho muda
        self.atualizar_btn_person() # Redesenho o btn, para acertar posicao

    # def on_press(self, *args):
    #     self.cor = self.cor_pressed
        #esta funcao reservada do kivy só funcionara para classe BUTTON do kivy

    def on_cor(self, *args):
        #Esta funcao reservada do kivy traz todos os eventos de mundanca que 
        #ocorrem em uma LIST PROPERTY de COR do kivy
        self.atualizar_btn_person()    
            #como houve uma mudanca nas cores, eu executo a funcao de atualizar o canvas,
            #isto fara o canvas ler novamente a propriedade cor

    def atualizar_btn_person(self, *args, **kwargs): # Criado funcao para desenhar o btn
        self.canvas.before.clear() # Para apagar rastros do redesenho do canvas em mseg que acontece   
        with self.canvas.before: # A maneira de buscar o funcao canvas é com 'With' e o uso do before é para ele ser 
                        #desenhado antes de qq coisa para ficar por baixo do label que usei no .kv
            Color(rgba=self.cor)
            # Os self abaixo são para assumir o tamanho que o próprio boxlayout reserva para ele no .kv, assim
            #fica mais facil posicionarmos e ajustarmos o tamanho
            Ellipse(
                    size=(self.height, self.height),
                    pos=(self.x, self.center_y-(self.height/2))                 
                    )
            Ellipse(
                    size=(self.height, self.height),
                    pos=(self.width-(self.height/2), self.center_y-(self.height/2))
                    )
            Rectangle(
                size=((self.width-self.height),self.height),
                pos=(self.x+(self.height/2), self.center_y-(self.height/2))
                      )
            x = self.width
            print(x)
            
    def on_touch_down(self, touch): # Esta é uma funcao reservada do kivy, ele pega todos os eventos de toque na tela 
        #toda. Usei ela pq não consegui usar o on_press somente dentro do desenho do canvas. O touch como atributo me
        #entrega dois atributos em lista, spos e pos, dentro deles eu tenho o x e y do toque. Usei a condição abaixo 
        #para prosseguir somente se o toque for dentro do tamanho do canvas desenhado, dentro de suas coordenadas x,y
        if touch.pos[0] > self.x and touch.pos[0] < self.width+5:
            if touch.pos[1] > self.center_y-25 and touch.pos[1] < self.center_y+25:
                #print(touch.pos[0])
                #App.get_running_app().root.current = 'tarefas'
                    #Neste eu consigo navegar entre os niveis de objeto. APP.get_running_app() eu recebo o objeto
                    # que é meu APP principal, visto no print_1 abaixo. Adicionando a linha o .ROOT, eu chego no objeto filho
                    # o meu GERENCIADOR_TELA que é a classe onde tudo começa e então posso usar os recursos de trocar de tela 
                print(f'PRINT_1 : {App.get_running_app()}')
                print(f'PRINT_2 : {App.get_running_app().root}')
                print(f'Olha aqui ======>>>>> {self.text}')
                self.cor, self.cor_pressed = self.cor_pressed, self.cor 
                #Faco o cor de botao apertado ser assumida quando apertor o BTN Personalizado, com esta tecnica eu troco os 
                #valores de uma cor pela outro e torno a troca novamente na funcao ON_TOUCH_UP
                return True
        # print(dir(self)) # Apresenta todas subclasses do SELF
            
    def on_touch_up(self, touch): # Esta é uma funcao reservada do kivy, ele pega todos os eventos de toque na tela 
        #toda. Usei ela pq não consegui usar o on_press somente dentro do desenho do canvas. O touch como atributo me
        #entrega dois atributos em lista, spos e pos, dentro deles eu tenho o x e y do toque. Usei a condição abaixo 
        #para prosseguir somente se o toque for dentro do tamanho do canvas desenhado, dentro de suas coordenadas x,y
        if touch.pos[0] > self.x and touch.pos[0] < self.width+5:
            if touch.pos[1] > self.center_y-25 and touch.pos[1] < self.center_y+25:
                if self.text == 'Ver Tarefas':
                    App.get_running_app().root.current = 'tarefas'
                        #Neste eu consigo navegar entre os niveis de objeto. APP.get_running_app() eu recebo o objeto
                        # que é meu APP principal, visto no print_1 abaixo. Adicionando a linha o .ROOT, eu chego no objeto filho
                        # o meu GERENCIADOR_TELA que é a classe onde tudo começa e então posso usar os recursos de trocar de tela
                    print(touch.pos[0])               
                    print(f'PRINT_1 : {App.get_running_app()}')
                    print(f'PRINT_2 : {App.get_running_app().root}')
                    self.cor, self.cor_pressed = self.cor_pressed, self.cor #Faco o cor de botao apertado ser assumida quando apertor o BTN Personalizado
                    return True
                elif self.text == 'Assistente':
                    print('========>>> Apertei no Assistente Mane <<<=========')
                    self.cor, self.cor_pressed = self.cor_pressed, self.cor 
                    return True
        
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