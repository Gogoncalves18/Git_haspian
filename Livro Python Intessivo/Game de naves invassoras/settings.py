class Settings():
    """Classe para armazenar as configurações do jogo"""
    def __init__(self):
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (0,0,230)
        self.ship_speed_factor = 1.5
        #Configurações dos projeteis da espaçonave
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 69, 0
        self.bullets_allowed = 3 #tiros permitido no carregador da nave