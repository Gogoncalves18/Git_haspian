import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    """Classe para administrar os projeteis disparados"""
    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto para o projetil na posição atual da espaçonave"""
        super(Bullet, self).__init__() 
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) #Aqui usamos a classe rect para criar um projetil 
        #com posição x,y em 0,0. E também criamos um tamanho para ele. Sua posição irá casar com a espaçonave nas próximas linhas
        self.rect.centerx = ship.rect.centerx #Aqui colocamos o centro em x do projetil na mesma orientação que o centro x do a ship
        self.rect.top = ship.rect.top #aqui posiciono o top dela com o top da nave, portanto o projetil ficará tapado pela nave
        self.y = float(self.rect.y) #Armazena a posicao do projetil como decimal
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor    
    
    def update(self):
        """Move o projetil para cima na tela"""
        self.y -= self.speed_factor #Movimento o pix em Y de acordo com o atributo speed_factor em settings
        self.rect.y = self.y #atualizo a posição na tela

    def draw_bullet(self):
        """desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)