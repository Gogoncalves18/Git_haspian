import pygame

# C
COR_LARANJA = (255, 128, 0)
COR_BRANCA = (255, 255, 255)
COR_AMARELO = (255, 255, 128)
COR_VERDE = (0, 128, 0)
COR_CYANO = (0, 128, 128)

# E
ENTITY_SPEED = {
    'L1_bg_0': 0,
    'L1_bg_1': 1,
    'mago': 5,
    'ghost_1': 2,
    'ghost_2': 4,
    'ghost_3': 6
}

ENTITY_SCORE = {
    'L1_bg_0': 0,
    'L1_bg_1': 0,
    'mago': 0,
    'ghost_1': 0,
    'ghost_2': 0,
    'ghost_3': 0
}

EVENT_GHOST = pygame.USEREVENT + 1  # Const do pygame para uso de tempo
EVENT_TIMEOUT = pygame.USEREVENT + 2  # Const do pygame para uso de tempo
EVENT_TIME_GHOST = 1000
EVENT_TIMEOUT_STEP = 100  # Dominiu do tempo do level
EVENT_TIMEOUT_LEVEL = 10000  # Tempo do level

# E
ENTITY_HEALTH = {
    'ghost_1': 3,
    'ghost_2': 3,
    'ghost_3': 3,
    'mago': 1,
    'L1_bg_0': 300,
    'L1_bg_1': 300,
}

# M
MENU_OPTION = ('PLAY',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 1200
WIN_HEIGHT = 675

# Adendos

SCORE_POS = {
    'Title': (WIN_WIDTH/2, 100),
    'Entername': (WIN_WIDTH/2, 150),
    'Label': (WIN_WIDTH/2, 200),
    'Name': (WIN_WIDTH/2, 230),
    'Cab': (WIN_WIDTH/2, (WIN_HEIGHT/2)-15),
    'Pontos': (WIN_WIDTH/2, (WIN_HEIGHT/2)+30),
    0: (WIN_WIDTH/2, (WIN_HEIGHT/2)+50),
    1: (WIN_WIDTH/2, (WIN_HEIGHT/2)+100),
    2: (WIN_WIDTH/2, (WIN_HEIGHT/2)+150),
    3: (WIN_WIDTH/2, (WIN_HEIGHT/2)+200),
    4: (WIN_WIDTH/2, (WIN_HEIGHT/2)+250),
    5: (WIN_WIDTH/2, (WIN_HEIGHT/2)+300)
}

PATH = 'C:/git/Git_haspian/Uninter/Linguagem_programacao/Trabalho/entities/asset/'
