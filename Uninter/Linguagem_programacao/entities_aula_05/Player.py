from entities.Entity import Entity
import pygame.key
from entities.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, \
                           PLAYER_K_DOWN, PLAYER_K_UP, PLAYER_K_RIGHT, \
                           PLAYER_K_LEFT, PLAYER_K_SHOOT, ENTITY_SHOT_DELAY
from entities.Player_Shot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_K_UP[self.name]] and self.rect.top > 0:
            # Para subir a nave
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_K_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            # Para descer a nava até o limite
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_K_LEFT[self.name]] and self.rect.left > 5:
            # Para descer a nava até o limite
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_K_RIGHT[self.name]] and self.rect.right < (WIN_WIDTH - 5):
            # Para descer a nava até o limite
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_k = pygame.key.get_pressed()
            if pressed_k[PLAYER_K_SHOOT[self.name]]:
                # Instania para gerar o tiro de laser
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
