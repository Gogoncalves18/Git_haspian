from entities.Background import BackGround
from entities.const import WIN_WIDTH, WIN_HEIGHT
from entities.Player import Player
from entities.Enemy import Enimy
import random


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        # um laco usando match para ler o tipo de item
        match entity_name:
            # Neste caso pego as imagens de asset
            case 'Level1Bg':
                # preparo uma lista vazia para receber os obj
                list_bg = []
                # Lanço com o mesmo numero de imagens no asset
                for i in range(7):
                    # Adiciono os obj que instancio do background
                    list_bg.append(BackGround(name=f'Level1Bg{i}', position=(0, 0)))
                    # Gero mais sete imagens para ficar repetindo
                    list_bg.append(BackGround(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))

                return list_bg
            
            case 'Level2Bg':
                # preparo uma lista vazia para receber os obj
                list_bg = []
                # Lanço com o mesmo numero de imagens no asset
                for i in range(5):
                    # Adiciono os obj que instancio do background
                    list_bg.append(BackGround(name=f'Level2Bg{i}', position=(0, 0)))
                    # Gero mais sete imagens para ficar repetindo
                    list_bg.append(BackGround(name=f'Level2Bg{i}', position=(WIN_WIDTH, 0)))

                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))
            
            case 'Player2':
                return Player('Player2', (10, ((WIN_HEIGHT / 2)-40)))
            
            case 'Enemy1':
                return Enimy('Enemy1', ((WIN_WIDTH - 5), random.randint(15, (WIN_HEIGHT - 10))))
            
            case 'Enemy2':
                return Enimy('Enemy2', ((WIN_WIDTH - 5), random.randint(15, (WIN_HEIGHT - 10))))
