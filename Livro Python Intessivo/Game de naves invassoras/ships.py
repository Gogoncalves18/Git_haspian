import pygame
class Ship():
    """Classe para criação de espacionaveis espaciais"""
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/Game de naves invassoras/imagens/my_ship.png') #Metodo de pygame para carregar imagens, tem que cuidar, o pygame trabalha melhor com .bmp
        self.rect = self.image.get_rect() #Criamos um atributo com o metodo rect() pois o pygame cria uma camada para o objeto na tela onde o calculo é um retangulo
        self.screen_rect = screen.get_rect() #Obtenho o tamanho da tela e passo par ao objeto screen
        self.rect.centerx = self.screen_rect.centerx #Alinho o x da tela com o x da espaçonave
        #Os objetos rect podem ser transladados por referẽncias pelas bordas superiores, inferiores, lados, ou pelo centro do objeto.Isto permite maior facilidade nos calculos
        self.rect.bottom = self.screen_rect.bottom #Alinho a parte debaixo da tela com a espaçonave
        self.moving_right = False #flag para saber se a espaçonave está parada ou movendo
        self.moving_left = False

    
    def blitme(self):
        """Desenha a espaçonava em sua posição atual"""
        self.screen.blit(self.image, self.rect)      

    def update(self):
        """Atualiza a posicao da espaçonave de acordo com a flag moving"""
        if self.moving_right: 
            self.rect.centerx += 1  #Jogo a imagem 1 pix para direita em relação ao ponto que ela começou, ela estava no centro da tela
        elif self.moving_left:
            self.rect.centerx -= 1 #Jogo a imagem 1 pix para esquerda em relação ao ponto que ela começou, ela estava no centro da tela ou ao ultimo ponto