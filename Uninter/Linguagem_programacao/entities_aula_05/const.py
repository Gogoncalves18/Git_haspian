import pygame.key
import pygame


# C
COR_LARANJA = (255, 128, 0)
COR_BRANCA = (255, 255, 255)
COR_AMARELO = (255, 255, 128)
COR_VERDE = (0, 128, 0)
COR_CYANO = (0, 128, 128)

# E
ENTITY_HEALTH = {
    'Level1Bg0': 300,
    'Level1Bg1': 300,
    'Level1Bg2': 300,
    'Level1Bg3': 300,
    'Level1Bg4': 300,
    'Level1Bg5': 300,
    'Level1Bg6': 300,
    'Level2Bg0': 300,
    'Level2Bg1': 300,
    'Level2Bg2': 300,
    'Level2Bg3': 300,
    'Level2Bg4': 300,
    'Level2Bg5': 300,
    'Level2Bg6': 300,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1
}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Level2Bg5': 5,
    'Level2Bg6': 6,
    'Player1': 3,
    'Player2': 3,
    'Player1Shot': 3,
    'Player2Shot': 3,
    'Enemy1': 2,
    'Enemy2': 1,
    'Enemy1Shot': 3,
    'Enemy2Shot': 3
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 80,
    'Enemy2': 65,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Player1': 1,
    'Player2': 1,
    'Player1Shot': 25,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 20,
    'Enemy2Shot': 15
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Level2Bg5': 0,
    'Level2Bg6': 0,
    'Player1': 0,
    'Player2': 0,
    'Player1Shot': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy1Shot': 0,
    'Enemy2Shot': 0
}

EVENT_ENEMY = pygame.USEREVENT + 1  # Const do pygame para uso de tempo
EVENT_TIMEOUT = pygame.USEREVENT + 2  # Const do pygame para uso de tempo
EVENT_TIME_ENEMY = 4000
EVENT_TIMEOUT_STEP = 100
EVENT_TIMEOUT_LEVEL = 20000

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_K_UP = {'Player1': pygame.K_UP,
               'Player2': pygame.K_w,
               'Enemy1': 0}
PLAYER_K_DOWN = {'Player1': pygame.K_DOWN,
                 'Player2': pygame.K_s,
                 'Enemy1': 0}
PLAYER_K_LEFT = {'Player1': pygame.K_LEFT,
                 'Player2': pygame.K_a,
                 'Enemy1': 0}
PLAYER_K_RIGHT = {'Player1': pygame.K_RIGHT,
                  'Player2': pygame.K_d,
                  'Enemy1': 0}
PLAYER_K_SHOOT = {'Player1': pygame.K_SPACE,
                  'Player2': pygame.K_SPACE,
                  'Enemy1': 0}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
