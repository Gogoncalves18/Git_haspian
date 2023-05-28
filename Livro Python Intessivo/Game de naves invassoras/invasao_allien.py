import pygame
from settings import Settings
from ships import Ship
import game_functions as gf
from pygame.sprite import Group #Esta classe se comporta como uma lista e tem algumas funcionalidades importante para o projetil
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game(): #Inicializa o jogo e cria obj para tela
    pygame.init() #Inicialização das funções do Pygame em segundo plano
ai_settings = Settings() #Armazenei a classe de configurações do arquivo settings.py na variável para usar ao longo do jogo
stats = GameStats(ai_settings) #Para iniciar a instacia que fará os dados statistico
screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height)) #Criamos uma janela de exibição para o jogo
sb = Scoreboard(ai_settings, screen, stats) #Instanciado o placar de pontos ganhos
pygame.display.set_caption("Invasão Alien") #Titulo da janela do jogo
play_button = Button(ai_settings, screen, "Play")
ship = Ship(ai_settings, screen) #cria uma espaçonave antes do while para não criar uma espaçonave a cada laço
bullets = Group() #Cria um grupo ao qual serão armazenado os projeteis, como se fosse uma instancia
bg_color = ai_settings.bg_color #Cor para tela fundo
#alien = Alien(ai_settings, screen)
aliens = Group() #Grupo da frota de aliens
gf.create_fleet(ai_settings, screen, ship, aliens)
while True:
    gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) # Função para pegar os eventos do teclado, aqui inicia os modulos de objetos de nave e projeteis
    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets) #Chama a funcao para atualizar os projeteis em game_functions
        gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets) #Chama o metodo para atualizar a posição dos aliens dentro do grupo aliens
        #E controlar o numero de vidas e reconstruir a frota alien quando ela atingir a nave
    gf.update_screen(ai_settings, bg_color, screen, stats, sb, ship, aliens, bullets, play_button) #aqui atualizo a tela com os objetos
    run_game() #puxa o metodo que inicializa o jogo e entra no laço principal

