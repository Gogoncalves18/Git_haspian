import datetime
import pygame
import sys
from pygame import K_BACKSPACE, K_ESCAPE, K_RETURN, KEYDOWN, Surface, Rect
from pygame.event import EventType
from pygame.font import Font
from entities.const import COR_AMARELO, SCORE_POS, MENU_OPTION, COR_BRANCA, COR_CYANO
from entities.DBProxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        # Define o carregamento da imagem
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/asset/ScoreBg.png').convert_alpha()
        # Define uma area para receber uma imagem que comeca no canto da tela
        # superior
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, game_mode: str, player_placar: list[int]):
        pygame.mixer_music.load('./Uninter/Linguagem_programacao/asset/Score.mp3')
        pygame.mixer_music.play(-1)
        # Conexao com o BD para tratar os pontos salvos
        db_proxy = DBProxy('DBScore')        
        nome_reg = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=48, text='Você Ganhou!', text_color=COR_AMARELO, text_center_pos=SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_placar[0]
                text = 'Player 1 - entre com seu nome (4 letras):'
            if game_mode == MENU_OPTION[1]:
                score = (player_placar[0] + player_placar[1]) / 2
                text = 'Dupla - entre com seu nome (4 letras):'
            if game_mode == MENU_OPTION[2]:
                # max() pega o maior valor de uma lista
                score = max(player_placar)
                text = 'Vencedor - entre com seu nome (4 letras):'
            # Escrever o texto na tela    
            self.score_text(text_size=20, text=text, text_color=COR_BRANCA, text_center_pos=SCORE_POS['Entername'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(nome_reg) == 4:
                        print({'name': nome_reg, 'score': score, 'date': get_formatted_date()})
                        db_proxy.save({'name': nome_reg, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == K_BACKSPACE:
                        nome_reg = nome_reg[:-1]
                    else:
                        if len(nome_reg) < 4:
                            nome_reg += event.unicode
            self.score_text(text_size=20, text=nome_reg, text_color=COR_CYANO, text_center_pos=SCORE_POS['Name'])
            pygame.display.flip()

    def show_score(self):
        pygame.mixer_music.load('./Uninter/Linguagem_programacao/asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(text_size=20, text='TOP 10 SCORE', text_color=COR_AMARELO, text_center_pos=SCORE_POS['Title'])
        self.score_text(text_size=20, text='NOME     SCORE      DATA', text_color=COR_AMARELO, text_center_pos=SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.select_top10()
        db_proxy.close()

        for p in list_score:
            id, nome, score, data = p
            self.score_text(text_size=20, text=f'{nome}     {score}      {data}', text_color=COR_BRANCA, text_center_pos=SCORE_POS[list_score.index(p)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    dt_atual = datetime.date.today()
    tempo = dt_atual.strftime("%H:%M")
    data = dt_atual.strftime("%d/%m/%y")
    return f'{tempo} - {data}'
