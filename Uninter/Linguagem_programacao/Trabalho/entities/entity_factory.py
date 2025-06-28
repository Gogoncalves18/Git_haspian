from Trabalho.entities.background import BackGround
from Trabalho.entities.var import WIN_HEIGHT, WIN_WIDTH
from Trabalho.entities.Player import Player
from Trabalho.entities.ghosts import Ghost
import random


class EntityFactory:

    @staticmethod
    def obter_entidade(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'L1_bg_':
                list_imagens_bg = []
                for i in range(2):
                    if i == 1:
                        list_imagens_bg.append(BackGround(name=f'L1_bg_{i}',
                                                          position=(
                                                    (WIN_WIDTH / 2)-100, 50)))
                    else:
                        list_imagens_bg.append(BackGround(name=f'L1_bg_{i}',
                                                          position=(0, 0)))

                return list_imagens_bg

            case 'mago':
                return Player('mago', (10, WIN_HEIGHT / 2))

            case 'ghost1':
                return Ghost('ghost_1', (random.randint(100, WIN_WIDTH-100),
                                         230))
            case 'ghost2':
                return Ghost('ghost_2', (random.randint(100, WIN_WIDTH-100),
                                         230))
            case 'ghost3':
                return Ghost('ghost_3', (random.randint(100, WIN_WIDTH-100),
                                         230))
