import sys, pygame
from settings import Settings
from ships import Ship


def run_game(): #Inicializa o jogo e cria obj para tela
    pygame.init() #Inicialização das funções do Pygame em segundo plano
ai_settings = Settings() #Armazenei a classe de configurações do arquivo settings.py na variável para usar ao longo do jogo
screen = pygame.display.set_mode((ai_settings.screen_with,ai_settings.screen_height)) #Criamos uma janela de exibição para o jogo
pygame.display.set_caption("Invasão Alien")
ship = Ship(screen) #cria uma espaçonave antes do while para não criar uma espaçonave a cada laço
bg_color = ai_settings.bg_color #Cor para tela fundo
while True:
    for event in pygame.event.get(): #Este laço pega todos eventos que vem do teclado do sistema quando o usuario joga, assim criamos condicionais com os eventos que estamos lendo
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color) #Metodo para preencher cor na janela
    ship.blitme() #Desenhamos a espaçonave depois de preencher o fundo assim a espaçonave aparecerá
    pygame.display.flip() #Este metodo atualiza a janela sempre para a mais recente sempre que passo pelo laço while. Assim os elementos recebem no posição o que dá ideia de movimento
    run_game() #puxa o metodo que inicializa o jogo e entra no laço principal