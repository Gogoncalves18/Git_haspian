from Trabalho.entities.entity import Entity
from Trabalho.entities.var import WIN_HEIGHT
from Trabalho.entities.Player import Player
from Trabalho.entities.ghosts import Ghost


class Entity_Mediator:

    @staticmethod
    def verifcador_colisao(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]

            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                if isinstance(entity1, Ghost) and isinstance(entity2, Player):
                    # print('Passei na ENT 1')
                    Entity_Mediator.__verificador_colisao_entity(
                        entity1, entity2
                        )
                if isinstance(entity2, Ghost) and isinstance(entity1, Player):
                    # print('Passei na ENT 2')
                    Entity_Mediator.__verificador_colisao_entity(
                        entity1, entity2
                        )

    @staticmethod
    def __verificador_colisao_entity(ent1: Entity, ent2: Entity):
        if ent1.rect.right >= ent2.rect.left and \
               ent1.rect.left <= ent2.rect.right and \
               ent1.rect.bottom >= ent2.rect.top and \
               ent1.rect.top <= ent2.rect.bottom:
            if isinstance(ent1, Ghost):
                ent1.health = 0
                ent2.placar += 1
                return True
            else:
                ent2.health = 0
                ent1.placar += 1
                return True

    @staticmethod
    def verificador_limite_tela(entity_list: list[Entity],
                                ghost_invasores: list[Entity]
                                ):
        for ent in entity_list:
            if isinstance(ent, Ghost):
                # print('passei por aqui')
                if ent.rect.bottom > WIN_HEIGHT:
                    # print('>>>>>>>>>>>>>>>>>>>>   Fastama:  <<<<<<<<<<<<')
                    ent.health = 0
                    ghost_invasores.append(ent)

    @staticmethod
    def verificador_vida(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
