from entities.Entity import Entity
from entities.Enemy import Enimy
from entities.Player_Shot import PlayerShot
from entities.EnemyShot import EnemyShot
from entities.const import WIN_WIDTH
from entities.Player import Player


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
    # Metodo para verificar se o inimigo ja passou na tela
    # recebo como entrada objetos da classe entidade
    def __verificador_colisao_entity(ent1: object, ent2: object):
        valid_colision = False
        # Validar colisao de tiros e naves, verifico com a funcao isinstance se a ent1
        # é um obj do type Enimy e se a ent2 é do type PlayerShot
        if isinstance(ent1, Enimy) and isinstance(ent2, PlayerShot):
            valid_colision = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enimy):
            valid_colision = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_colision = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_colision = True

        if valid_colision:
            if ent1.rect.right >= ent2.rect.left and \
               ent1.rect.left <= ent2.rect.right and \
               ent1.rect.bottom >= ent2.rect.top and \
               ent1.rect.top <= ent2.rect.bottom:
                # Diminui a vida apartir do dano de colisao
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __placar(enemy: Enimy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            # Varre a lista de obj para encontrar o player1 e dar o score para ele
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.placar += enemy.placar
                elif ent.name == 'Player2':
                    ent.placar += enemy.placar

    @staticmethod
    def verificador_colisao(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            Entity_Mediator.__verificador_limite_tela(entity1)
            # Laço para pegar outra entidade para comparar para a colisao
            # Executo o "i+1" no codigo para pular o laço para frente, nao
            # repetindo o obj com ele mesmo na lista
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                Entity_Mediator.__verificador_colisao_entity(entity1, entity2)

    @staticmethod
    def verificador_vida(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                # Verifica se houve colisao com inimigo para descontar a vida
                if isinstance(ent, Enimy):
                    Entity_Mediator.__placar(ent, entity_list)
                entity_list.remove(ent)
