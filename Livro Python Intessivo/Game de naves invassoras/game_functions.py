import sys, pygame
from bullet import Bullet 
#Aqui eu crio o objeto projetil na tela
def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos provinientes do teclado"""
    for event in pygame.event.get(): #Este laço pega todos eventos que vem do teclado do sistema quando o usuario joga, assim criamos condicionais com os eventos que estamos lendo
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #Evento de keydown é de tecla pressionada, key up é de tecla solta
            check_keydown_events(event, ai_settings, screen, ship, bullets) #Aciono a função que corresponde a pressionar o teclado, dando a ele o evento e a ship
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a eventos que pressiona o teclado"""
    if event.key == pygame.K_RIGHT: #Identificando a tecla da direita
        ship.moving_right = True #altera o atributo dentro da classe Ship para fazer a espaçonave andar para esquerda
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets) #Função deste mesmo módulo que cuida da qtd de tiros que posso disparar

def check_keyup_events(event, ship):
    """Responde a eventos que solta o teclado"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
     

def update_screen(ai_settings, bg_color, screen, ship, bullets):
    """Atualiza as imagens na tela e altera para nova tela como um refresh"""
    screen.fill(bg_color) #Metodo para preencher cor na janela
    for bullet in bullets.sprites(): #aqui eu pego a lista que tem os projeteis armazenados e uso um metodo desta da classe Group que varre a lista
        bullet.draw_bullet() #aqui eu desenho na tela cada objeto, que usa uma função herdada no modulo bullet.py que atua sobre a classe Sprite
    ship.blitme() #Desenhamos a espaçonave depois de preencher o fundo assim a espaçonave aparecerá
    pygame.display.flip() #Este metodo atualiza a janela sempre para a mais recente sempre que passo pelo laço while. Assim os elementos recebem no posição o que dá ideia de movimento


def update_bullets(bullets):
    """Atualiza a posição dos projeteis e elimina os projeteis que atingiram o limite da tela"""
    bullets.update() #Este metodo chama a atualização de cada objeto colocado dentro da Função Group de pygame.sprite
    for bullet in bullets.copy():#Como não é recomendado modificar a lista em um laço, fizemos uma cópia para mante-la integra e mesmo assim ela fica referenciada
        if bullet.rect.bottom <= 0: #Aqui valido se ela chegou ao top da tela
            bullets.remove(bullet) #Removo o tiro que foi instaciado 
        #print(len(bullets)) #Aqui valido se a quantidade de tiros disparado está sendo eleminada da lista

def fire_bullet(ai_settings, screen, ship, bullets):
     """Controle a qtd de tiros que posso efetuar até que os mesmos rompam o limite da tela"""
     if len(bullets) < ai_settings.bullets_allowed: #Valido se os tiros disparados não atingiram a qtd de tiros da nave até o tiro atravessar a tela toda, depois recarrega
            new_bullet = Bullet(ai_settings, screen, ship) #Cria um novo projetil e adiciona ao grupo de projeteis
            bullets.add(new_bullet) #Cada objeto do projetil vai para o grupo bullets no código principal através do metodo add que é da classe Group