from pygame import Surface
from Trabalho.entities.entity import Entity
from Trabalho.entities.entity_factory import EntityFactory
import pygame
import sys
from Trabalho.entities.Player import Player
from Trabalho.entities.ghosts import Ghost
# from Trabalho.entities.background import BackGround
from Trabalho.entities.var import EVENT_GHOST, EVENT_TIME_GHOST, \
                                  EVENT_TIMEOUT, EVENT_TIMEOUT_STEP, \
                                  EVENT_TIMEOUT_LEVEL
import random
from Trabalho.entities.EntityMediator import Entity_Mediator
from pygame import Rect
import pygame.image
from pygame.font import Font
from Trabalho.entities.var import COR_AMARELO, COR_LARANJA, WIN_WIDTH


class Level:
    def __init__(self, janela: Surface, name: str):
        self.window = janela
        self.name = name
        # Primeiro eu gero a tipagem e depois defino o valor
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.obter_entidade(self.name +
                                                             '_bg_'))
        player = EntityFactory.obter_entidade('mago')
        player.placar = 0
        self.entity_list.append(player)
        self.lista_ghost_invasores: list[Entity] = []
        self.timeout = EVENT_TIMEOUT_LEVEL
        self.level = 1
        self.placar_mago = 0

        # Criacao dos ghost baseado no tempo do pygame
        pygame.time.set_timer(event=EVENT_GHOST, millis=EVENT_TIME_GHOST)
        pygame.time.set_timer(event=EVENT_TIMEOUT, millis=EVENT_TIMEOUT_STEP)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(40)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

                self.menu_text(text_size=18, text=f'\
                              Level: {self.level}',
                               text_color=COR_LARANJA,
                               text_center_pos=(50, 20))

                if isinstance(ent, Player):
                    self.menu_text(text_size=14, text=f'\
                                   Fantasmas Eliminados: {ent.placar}',
                                   text_color=COR_AMARELO,
                                   text_center_pos=(WIN_WIDTH / 2, 20))
                    self.placar_mago = ent.placar

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Gatilho para criar os ghosts baseado no tempo
                # da const "EVENT"
                if event.type == EVENT_GHOST:
                    # Sorteia qual dos inimigos vou injetar na lista de play
                    # choice = random.choice(('Enemy1', 'Enemy2'))
                    if self.level == 1:
                        self.entity_list.append(EntityFactory.obter_entidade(
                                                                    'ghost1'))
                    if self.level == 2:
                        self.entity_list.append(EntityFactory.obter_entidade(
                            f'ghost{random.randint(1, 2)}'))
                    if self.level == 3:
                        self.entity_list.append(EntityFactory.obter_entidade(
                            f'ghost{random.randint(1, 3)}'))

                # Controle para mudar de level
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= EVENT_TIMEOUT_STEP
                    if self.timeout == 0:
                        self.level += 1
                        self.timeout = EVENT_TIMEOUT_LEVEL

            for ent in self.entity_list:
                if isinstance(ent, Ghost):
                    self.menu_text(text_size=14, text=f'\
                                  Fantasmas Invasores: {
                                       len(self.lista_ghost_invasores)}',
                                   text_color=COR_AMARELO,
                                   text_center_pos=(WIN_WIDTH - 250, 20))

            # Envia para o mediador todos os objs que possuimos na lista de obj
            Entity_Mediator.verifcador_colisao(entity_list=self.entity_list)

            Entity_Mediator.verificador_limite_tela(
                entity_list=self.entity_list,
                ghost_invasores=self.lista_ghost_invasores
                )
            Entity_Mediator.verificador_vida(entity_list=self.entity_list)

            self.menu_text(text_size=14, text=f'\
                          Fantasmas Eliminados: {ent.placar}',
                           text_color=COR_AMARELO,
                           text_center_pos=(100, 600))
            self.menu_text(text_size=14, text=f'\
                          TEMPO: {self.timeout}',
                           text_color=COR_AMARELO,
                           text_center_pos=(100, 620))

            if self.level == 4:
                # print(' ++++++++++++++++++++++++++++++++++++++++++++ ')
                return [self.placar_mago, len(self.lista_ghost_invasores)]
            pygame.display.flip()

    # Funcao para desenhar textos na tela
    def menu_text(self, text_size: int, text: str, text_color: tuple,
                  text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter',
                                              size=text_size)
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
