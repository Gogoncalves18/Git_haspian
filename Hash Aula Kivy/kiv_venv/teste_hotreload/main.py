import os
from kaki.app import App
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.factory import Factory

class App_One(App, MDApp):

    KV_FILES = [
        os.path.join(os.getcwd(), 'lay_main_screen.kv')
    ]

    CLASSES = {
        "Tarefas": "main_screen"
    }

    AUTORELOADER_PATHS = [
        (os.getcwd(), {"recursive":True})
    ]

    def build_app(self):
        Window.size = [350, 560] 
        return Factory.Tarefas()
    
App_One().run()