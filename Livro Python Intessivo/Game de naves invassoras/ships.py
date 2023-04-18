import pygame
class Ship():
    """Classe para criação de espacionaveis espaciais e define sua posicao inicial"""
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('/home/gog/Documentos/Python/Git_haspian/Livro Python Intessivo/Game de naves invassoras/imagens/my_ship.png') #Metodo de pygame para carregar imagens, tem que cuidar, o pygame trabalha melhor com .bmp
        self.rect = self.image.get_rect() #Criamos um atributo com o metodo rect() pois o pygame cria uma camada para o objeto na tela onde o calculo é um retangulo
        self.screen_rect = screen.get_rect() #Obtenho o tamanho da tela e passo par ao objeto screen
        self.rect.centerx = self.screen_rect.centerx #Alinho o x da tela com o x da espaçonave
        #Os objetos rect podem ser transladados por referẽncias pelas bordas superiores, inferiores, lados, ou pelo centro do objeto.Isto permite maior facilidade nos calculos
        self.rect.bottom = self.screen_rect.bottom #Alinho a parte debaixo da tela com a espaçonave
        self.center = float(self.rect.centerx) #Aqui defino um valor decimal para a posicao da espaconave
        self.moving_right = False #flag para saber se a espaçonave está parada ou movendo
        self.moving_left = False

    
    def blitme(self):
        """Desenha a espaçonava em sua posição atual"""
        self.screen.blit(self.image, self.rect)      

    def update(self):
        """Atualiza a posicao da espaçonave de acordo com a flag moving"""
        if self.moving_right and self.rect.right < self.screen_rect.right: #rect.right retorna o valor que a imagem se encontra na tela e screen rect.right o tamanho da tela 
            #self.rect.centerx += 1  #Jogo a imagem 1 pix para direita em relação ao ponto que ela começou, ela estava no centro da tela
            self.center += self.ai_settings.ship_speed_factor            
        elif self.moving_left and self.rect.left > 0:
            #self.rect.centerx -= 1 #Jogo a imagem 1 pix para esquerda em relação ao ponto que ela começou, ela estava no centro da tela ou ao ultimo ponto
            self.center -= self.ai_settings.ship_speed_factor        
        self.rect.centerx = self.center #Atualizo o valor da posição da imagem pela relação de centro dela com a tela chamada screen