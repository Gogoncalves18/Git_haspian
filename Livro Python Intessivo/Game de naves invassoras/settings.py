class Settings():
    """Classe para armazenar as configurações do jogo"""
    def __init__(self):
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (0,0,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #Configurações dos projeteis da espaçonave
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 69, 0
        self.bullets_allowed = 3 #tiros permitido no carregador da nave
        #Configurações dos aliens
        self.alien_speed_factor = 1 #Define a velocidade de movimento lateral na linha da tela
        self.fleet_drop_speed = 100 #define a velocidade de descida dos aliens na tela
        self.fleet_direction = 1 #Onde 1 é direita e -1 é esquerda