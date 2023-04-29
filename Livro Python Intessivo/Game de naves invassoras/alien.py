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

    def update(self):
        """Atualiza a posicao dos objetos aliens"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction) #Aqui além de definir a velocidade, também definimos a direção
        self.rect.x = self.x
        
    def check_edges(self):
        """Validar se o alien está a borda da tela"""
        screen_rect = self.screen.get_rect() #Capituro o tamanho do retangulo da tela. A saida deste dado é [0,0,1200,800]
        #print(screen_rect) #A saida deste dado é [0,0,1200,800]
        if self.rect.right >= screen_rect.right: #Valido se a posição do alien está igual ou maior que o lado direito da tela, o primeiro
            #que der esta informação, subo um valor verdadeiro para saber se devo mudar de direção de todo o grupo
            return True
        elif self.rect.left <= 0: #Faço a mesma coisa com o lado esquerdo
            return True
                 