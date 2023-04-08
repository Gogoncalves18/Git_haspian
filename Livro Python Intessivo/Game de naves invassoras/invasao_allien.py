import sys, pygame


def run_game(): #Inicializa o jogo e cria obj para tela
    pygame.init() #Inicialização das funções do Pygame em segundo plano
screen = pygame.display.set_mode((1200,800)) #Criamos uma janela de exibição para o jogo
pygame.display.set_caption("Invasão Alien")
bg_color = (0,0,134) #Cor para tela fundo
while True:
    for event in pygame.event.get(): #Este laço pega todos eventos que vem do teclado do sistema quando o usuario joga, assim criamos condicionais com os eventos que estamos lendo
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color) #Metodo para preencher cor na janela
    pygame.display.flip() #Este metodo atualiza a janela sempre para a mais recente sempre que passo pelo laço while. Assim os elementos recebem no posição o que dá ideia de movimento
    run_game() #puxa o metodo que inicializa o jogo e entra no laço principal