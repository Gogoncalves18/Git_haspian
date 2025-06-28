import pygame
from Trabalho.entities.var import WIN_HEIGHT, WIN_WIDTH, \
                                  MENU_OPTION
from Trabalho.entities.menu import Menu
from Trabalho.entities.level import Level
from Trabalho.entities.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            score = Score(self.window)
            # Menu para sair do jogo
            if menu_return == MENU_OPTION[2]:
                pygame.quit()
                quit()
            # Menu para jogar
            elif menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'L1')
                level_return = level.run()
                if level_return:
                    score.save_score(level_return)
            elif menu_return == MENU_OPTION[1]:
                score.show_score()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fecha a janela
                    quit()  # Encerra o pygame
