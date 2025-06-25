from abc import ABC, abstractmethod
import pygame.image
from entities.const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carregamento da imagem
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.placar = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self):
        pass
