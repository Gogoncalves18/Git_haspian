class Settings():
    """Classe para armazenar as configurações do jogo"""
    def __init__(self):
        #Configuracoes da tela
        self.screen_with = 1200
        self.screen_height = 800
        self.bg_color = (0,0,230)
        #Configuracoes da espaconave
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
        self.fleet_drop_speed = 10 #define a velocidade de descida dos aliens na tela
        self.fleet_direction = 1 #Onde 1 é direita e -1 é esquerda
        #Configuracoes do jogo
        self.speedup_scale = 1.2
        self.score_scale = 1.5 #Taxa usada para aumentar o numero de pontos quando mudamos de nivel
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Busca as config iniciais do jogo quando o jogo é reiniciado devido a perda total de vidas do jogador"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1 #Onde 1 é direita e -1 é esquerda
        self.alien_points = 50 #Vlr ganho para cada alien derrubado

    def increase_speed(self):
        """Aumenta as configuracoes de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) #Usado int para dar numeros inteiros a pontuacao
