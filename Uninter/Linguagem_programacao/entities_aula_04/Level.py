import sys
from entities.Entity import Entity
from entities.EntityFactory import EntityFactory
import pygame
from pygame.font import Font
from pygame import Surface, Rect
from entities.const import COR_BRANCA, WIN_HEIGHT, MENU_OPTION, \
                           EVENT_ENEMY, EVENT_TIME_ENEMY
import random
from entities.EntityMediator import Entity_Mediator
from entities.Player import Player
from entities.Enemy import Enimy


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []  # Primeiro eu gero a tipagem e depois defino o valor
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        # Defino se vou fabricar o player 2
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        # a cada "x" tempo criaremos um inimigo
        pygame.time.set_timer(EVENT_ENEMY, EVENT_TIME_ENEMY)

    def run(self):
        pygame.mixer_music.load(f'./Uninter/Linguagem_programacao/asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enimy)):
                    # Guardo na lista de obj em movimento apenas os 
                    # tiros dados por inimigos e player
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # Gatilho para criar os inimigos baseado no tempo da const "EVENT"
                if event.type == EVENT_ENEMY:
                    # Sorteia qual dos inimigos vou injetar na lista de play
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', text_color=COR_BRANCA, text_pos=(10, 5))        
            self.level_text(text_size=14, text=f'fps: {clock.get_fps():.0f}', text_color=COR_BRANCA, text_pos=(10, WIN_HEIGHT-35))
            self.level_text(text_size=14, text=f'entities: {len(self.entity_list)}', text_color=COR_BRANCA, text_pos=(10,  WIN_HEIGHT - 20))        
            pygame.display.flip()
            # Envia para o mediador todos os objs que possuimos na lista de obj
            Entity_Mediator.verificador_colisao(entity_list=self.entity_list)
            Entity_Mediator.verificador_vida(entity_list=self.entity_list)
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
