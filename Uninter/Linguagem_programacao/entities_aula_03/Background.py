from entities.Entity import Entity
from entities.const import WIN_WIDTH, ENTITY_SPEED


class BackGround(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Uma velocidade diferente para cada obj
        # Nova posicao da imagem quando ela chegar ao final da tela
        if self.rect.right <= 0:
            # Jogo o lado esquerdo da imagem na medida maxima da tela
            self.rect.left = WIN_WIDTH
