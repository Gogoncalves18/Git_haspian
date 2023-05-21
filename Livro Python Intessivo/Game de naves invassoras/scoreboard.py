import pygame.font
class Scoreboard():
    """Classe para mostrar infos sobre a pontuacao"""
    def __init__(self, ai_settings, screen, stats):
        """Inicializa os atributos da pontuacao"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #Configuracoes de fonte para as informacoes de pontuacao
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score() #Mostra a pontuacao atual
        self.prep_high_score() #Mostra a pontuacao total que ja foi atingida no game

    def prep_score(self):
        """Transforma a pontuacao em uma imagem redenrizada"""
        #A função round arrendonda um numero decimal com uma qtd definida de casas especificada no segundo argumento
        #Se no segundo argumento for passado um numero negativo, ele arredonda o valor para o multiplo mais proximo
        rounded_score = int(round(self.stats.score, -1)) #
        score_str = "{:,}".format(rounded_score) #Armazeno o valor numero em um texto para ser trabalhado pelo render
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color) # Função render para gerar um imagem
        #passamos o texto, cor texto e cor do fundo
        self.score_rect = self.score_image.get_rect() #busco o retangulo da imagem para posiciona-la na tela
        self.score_rect.right = self.screen_rect.right - 20 #Posiciono o lado direito da imagem com o lado direito da tela 
        self.score_rect.top = 20 # gero distancia da parte de cima da tela

    def show_score(self):
        """Metodo para exibir a imagem renderizada"""
        self.screen.blit(self.score_image, self.score_rect) #Desenho a imgame do score no local especificado em score_rect
        self.screen.blit(self.high_score_image, self.high_score_rect) # Desenha a imagem da pontacao maxima na tela

    def prep_high_score(self):
        """Transforma a pontuacao maxima em uma imagem renderizada"""
        high_score = int(round(self.stats.high_score, -1)) #Busca a info do modulo game_stats e arredonda em multiplo de 10
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect() #Busco o retangulo da imagem
        self.high_score_rect.centerx = self.screen_rect.centerx #Alinho a imagem do score com o centro da tela
        self.high_score_rect.top = self.score_rect.top #Alinho o Y da nova imagem com o Y da pontuação que já está funcionando

