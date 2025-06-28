from pygame import Surface, Rect
import pygame.image
from pygame.font import Font
from Trabalho.entities.var import COR_BRANCA, COR_AMARELO, \
                                  COR_LARANJA, WIN_WIDTH, \
                                  MENU_OPTION, WIN_HEIGHT, \
                                  PATH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/Trabalho/entities/asset/' + 'bckg_menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_number = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Desenho do titulo
            self.menu_text(text_size=50, text='PEGA FANTASMA',
                           text_color=COR_LARANJA,
                           text_center_pos=((WIN_WIDTH/2), 100))

            # Desenho do MENU
            for opcao in range(len(MENU_OPTION)):
                if opcao == menu_number:
                    self.menu_text(text_size=20, text=MENU_OPTION[opcao],
                                   text_color=COR_AMARELO,
                                   text_center_pos=((WIN_WIDTH/2),
                                                    (WIN_HEIGHT/2)+(50*opcao)))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[opcao],
                                   text_color=COR_BRANCA,
                                   text_center_pos=((WIN_WIDTH/2),
                                                    (WIN_HEIGHT/2)+(50*opcao)))
            # Atualiza a imagem na tela
            pygame.display.flip()

            # Check de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
                # Primeiro assume os eventos de teclado
                if event.type == pygame.KEYDOWN:
                    # Movimenta a cor do texto para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_number < len(MENU_OPTION)-1:
                            menu_number += 1
                    if event.key == pygame.K_UP:
                        if menu_number > 0:
                            menu_number -= 1
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_RETURN:
                        # Retorna para o GAME a opcao escolhida
                        # print(f'ENTRANDO NO JOGO: {MENU_OPTION[menu_number]}')
                        return MENU_OPTION[menu_number]

    # Funcao para desenhar textos na tela
    def menu_text(self, text_size: int, text: str, text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter',
                                              size=text_size)
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
