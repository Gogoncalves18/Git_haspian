import pygame
from settings import Settings
from ships import Ship
import game_functions as gf

def run_game(): #Inicializa o jogo e cria obj para tela
    pygame.init() #Inicialização das funções do Pygame em segundo plano
ai_settings = Settings() #Armazenei a classe de configurações do arquivo settings.py na variável para usar ao longo do jogo
screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height)) #Criamos uma janela de exibição para o jogo
pygame.display.set_caption("Invasão Alien")
ship = Ship(ai_settings, screen) #cria uma espaçonave antes do while para não criar uma espaçonave a cada laço
bg_color = ai_settings.bg_color #Cor para tela fundo
while True:
    gf.check_events(ship) # Função para pegar os eventos do teclado
    ship.update()
    gf.update_screen(bg_color, screen, ship)
    run_game() #puxa o metodo que inicializa o jogo e entra no laço principal