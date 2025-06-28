from Trabalho.entities.entity import Entity
import pygame
from Trabalho.entities.var import ENTITY_SPEED


class Ghost(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED[self.name]
