#Arquivo para fazer as importacoes e  configuração dos caminhos
import os #Para trazer o endereço dos arquivos
from kaki.app import App #Para fazer o hot reload
from kivy.core.window import Window #Para definir o tamanho de janela do kivy
from kivymd.app import MDApp #Necessário para funcionar o Kaki
from kivy.factory import Factory #Para ter acesso a classe que contem todas bibliotecas do kivy

class MDLive(App,MDApp): #Classe para herdar as classes kivy e MDKivy e construir os direcionamentos

    KV_FILES = [
        os.path.join(os.getcwd(), 'lay_tela.kv')
    ]
    # Aqui listamos os caminhos dos .KV que construi o layout das telas, para cada tela criada com o seu kv, 
    #preciso apontar nesta lista de endereço

    CLASSES = {
        "Tela": "screen_ui"
    }
    # Aqui aponto as classes necessárias, estas classes herdarão do Kivy as classes bases e apontarao para a estrutura .KV
    # Cada tela poderá ter sua classe sendo chamada, neste caso "Tela" é a funcao que está dentro do arquivo "screen_ui.py"
    #que constroi uma classe herdada do kivy e que conversará com o "lay_tela.kv"

    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive":True})
    ]
    # Defino o padrao do autoreloader, ao qual defino o caminho como recurvivo

    def build_app(self): #Funcao contrutora da tela do app
        Window.size = [350, 560] #Definicao do tamanho da tela, para ter proporcionalidade com o celular
        return Factory.Tela() #Aqui defino o retorno do contrutor o acesso a biblioteca que contem todas
                                #classes do kivy e sobre ela chamo a classe Tela() que me devolve as instrucoes construidas
    
MDLive().run() #Chamo a casse toda e deixo rodando
