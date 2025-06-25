from entities.Entity import Entity
from entities.Enemy import Enimy
from entities.Player_Shot import PlayerShot
from entities.EnemyShot import EnemyShot
from entities.const import WIN_WIDTH


class Entity_Mediator:

    @staticmethod
    # Metodo para verificar se o inimigo ja passou na tela
    # recebo como entrada objetos da classe entidade
    def __verificador_limite_tela(ent: Entity):
        # Faço uma validacao se o objeto é da class entity e
        # se ele é um inimigo
        if isinstance(ent, Enimy):
            # Valido a posicao dele e se chegar ao final da tela
            # altero o valor de vida dele para depois destroir o obj
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verificador_colisao(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            Entity_Mediator.__verificador_limite_tela(test_entity)

    @staticmethod
    def verificador_vida(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
