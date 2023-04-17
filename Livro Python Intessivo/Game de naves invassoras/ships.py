import pygame
class Ship():
    """Classe para criação de espacionaveis espaciais"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('imagens/ship_aliens.png') #Metodo de pygame para carregar imagens, tem que cuidar, o pygame trabalha melhor com .bmp
        self.rect = self.image.get_rect() #Criamos um atributo com o metodo rect() pois o pygame cria uma camada para o objeto na tela onde o calculo é um retangulo
        self.screen_rect = screen.get_rect() #Obtenho o tamanho da tela e passo par ao objeto screen
        self.rect.centerx = self.screen_rect.centerx #Alinho o x da tela com o x da espaçonave
        #Os objetos rect podem ser transladados por referẽncias pelas bordas superiores, inferiores, lados, ou pelo centro do objeto.Isto permite maior facilidade nos calculos
        self.rect.bottom = self.screen_rect.bottom #Alinho a parte debaixo da tela com a espaçonave


    def blitme(self):
        """Desenha a espaçonava em sua posição atual"""
        self.screen.blit(self.image, self.rect)        