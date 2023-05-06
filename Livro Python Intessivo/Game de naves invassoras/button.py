import pygame.font
pygame.font.init()
class Button():
    def __init__(self, ai_settings, screen, msg):
        """Inicializa os atributos de botao de inicio de jogo"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #Abaixo define as caracteristicas do botao
        self.width, self.heigth = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 48) #O Pygame.font é um atributo que renderiza o texto, quando passamos o arg NONE, ele usa um fonte padrao e 48 é o tamanho
        self.rect = pygame.Rect(0,0,self.width, self.heigth) #Constroi o objeto do botao
        self.rect.center = self.screen_rect.center #Centraliza o botao na tela 
        self.prep_msg(msg) #Chamamos a transformação de texto em imagem

    def prep_msg(self, msg):
        """Transforma a mensagem em imagem renderizada e centraliza o mesmo no botao"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #Transforma um texto em imagem com os seguintes args: 'texto', 'Ativa ou desativa
        #o metodo de antilinhas na borda da imagem', 'define a cor do texto', 'define a cor do botao'
        self.msg_image_rect = self.msg_image.get_rect() #Pego o tamanho retagular do objeto que acabei de criar
        self.msg_image_rect.center = self.rect.center #passei a posicao central da tela para o atributo que representará o centro da imagem

    def draw_button(self):
        """Desenha o botao em branco e em seguida desenha a mensagem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        