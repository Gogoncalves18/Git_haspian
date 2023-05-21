class GameStats():
    """Armazena dados estatistico da invasao alien"""
    def __init__(self, ai_settings):
        """Inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.high_score = 0 #Vlr pontuacao maxima, nunca deve ser reiniciada
        self.reset_stats()
        self.game_active = False #Flag para encerrar o jogo sempre que a vida acabar

    def reset_stats(self):
        """Inicializa os dados estatisticos que podem mudar ao longo do jogo"""
        self.ships_left = self.ai_settings.ship_limit #numero de vidas no jogo
        self.score = 0
    