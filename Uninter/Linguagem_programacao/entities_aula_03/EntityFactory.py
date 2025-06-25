from entities.Background import BackGround
from entities.const import WIN_WIDTH


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