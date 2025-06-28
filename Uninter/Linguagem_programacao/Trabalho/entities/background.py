from Trabalho.entities.entity import Entity
from Trabalho.entities.var import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED


class BackGround(Entity):

    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        if self.name == 'L1_bg_1':
            if self.rect.right >= 0:
                self.rect.centerx -= ENTITY_SPEED[self.name]
            else:
                self.rect.left = WIN_WIDTH
        self.rect.centerx -= ENTITY_SPEED[self.name]
