import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """Uma classe que representa um alienigena da frota"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/Game de naves invassoras/imagens/ship_aliens.png') #Metodo de pygame para carregar imagens, tem que cuidar, o pygame trabalha melhor com .bmp
        self.rect = self.image.get_rect() #Criamos um atributo com o metodo rect() pois o pygame cria uma camada para o objeto na tela onde o calculo é um retangulo
        self.rect.x = self.rect.width #Alinho o alien do lado esquerdo
        self.rect.y = self.rect.height #Alinho o alien na parte máxima superior
        self.x = float(self.rect.x)  
        
      
    def blitme(self):
        """Desenha o alien em sua posição atual"""
        self.screen.blit(self.image, self.rect)        