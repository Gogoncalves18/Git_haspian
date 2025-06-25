import pygame.image
from pygame import Surface, Rect
from pygame.font import Font
from entities.const import WIN_WIDTH, WIN_HEIGHT, COR_BRANCA, COR_LARANJA, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        # Define o carregamento da imagem
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/asset/MenuBg.png')
        # Define uma area para receber uma imagem que comeca no canto da tela
        # superior
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Uninter/Linguagem_programacao/asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenha a imagem na area estabelecida
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Mountain', COR_LARANJA, ((WIN_WIDTH/2), 70))
            self.menu_text(50, 'Shouter', COR_LARANJA, ((WIN_WIDTH/2), 120))

            for t in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[t], COR_BRANCA, ((WIN_WIDTH/2), 180 + 30 * t))


            # Atualiza a imagem na tela
            pygame.display.flip()
            # Check de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)