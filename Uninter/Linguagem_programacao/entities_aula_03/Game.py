import pygame
from entities.Menu import Menu
from entities.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from entities.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:  # Selecao das opções do jogo
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

            elif menu_return == MENU_OPTION[4]:  # Encerra o jogo
                pygame.quit()
                quit()
            else:
                pass
                
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
