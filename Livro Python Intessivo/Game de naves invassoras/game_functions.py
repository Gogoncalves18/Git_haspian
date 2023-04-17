import sys, pygame
def check_events(ship):
    """Responde a eventos provinientes do teclado"""
    for event in pygame.event.get(): #Este laço pega todos eventos que vem do teclado do sistema quando o usuario joga, assim criamos condicionais com os eventos que estamos lendo
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Evento de keydown é de tecla pressionada, key up é de tecla solta
            if event.key == pygame.K_RIGHT: #Identificando a tecla da direita
                ship.moving_right = True #altera o atributo dentro da classe Ship para fazer a espaçonave andar para esquerda
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
     

def update_screen(bg_color, screen, ship):
    """Atualiza as imagens na tela e altera para nova tela como um refresh"""
    screen.fill(bg_color) #Metodo para preencher cor na janela
    ship.blitme() #Desenhamos a espaçonave depois de preencher o fundo assim a espaçonave aparecerá
    pygame.display.flip() #Este metodo atualiza a janela sempre para a mais recente sempre que passo pelo laço while. Assim os elementos recebem no posição o que dá ideia de movimento