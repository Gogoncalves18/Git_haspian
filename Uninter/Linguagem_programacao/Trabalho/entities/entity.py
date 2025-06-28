from abc import ABC, abstractmethod
import pygame.image
from Trabalho.entities.var import ENTITY_HEALTH, ENTITY_SCORE, PATH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/Trabalho/entities/asset/' +
                                      name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.health = ENTITY_HEALTH[self.name]
        self.placar = ENTITY_SCORE[self.name]

    @abstractmethod
    def move():
        pass
    
