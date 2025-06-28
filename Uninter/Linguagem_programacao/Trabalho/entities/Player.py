from Trabalho.entities.entity import Entity
import pygame
from Trabalho.entities.var import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        pressed_k = pygame.key.get_pressed()
        if pressed_k[pygame.K_UP] and \
           self.rect.top > 5:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_k[pygame.K_DOWN] and \
           self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_k[pygame.K_LEFT] and \
           self.rect.left > 5:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_k[pygame.K_RIGHT] and \
           self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
