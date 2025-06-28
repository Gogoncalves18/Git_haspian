import pygame
from pygame import Surface, Rect
import sys
from Trabalho.entities.DBProxy import DBproxy
from pygame.font import Font
from Trabalho.entities.var import COR_CYANO, SCORE_POS, \
                                  COR_BRANCA, COR_VERDE, \
                                  COR_AMARELO, COR_LARANJA, \
                                  PATH


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./Uninter/Linguagem_programacao/Trabalho/entities/asset/' + 'score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save_score(self, placar_mago_ghost: list):
        db_prox = DBproxy('./Uninter/Linguagem_programacao'
                          '/Trabalho/fantasmas')
        nome_reg = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.score_text(text_size=48, text=f'Você fez: {placar_mago_ghost[0]} - Fantasma fez: {placar_mago_ghost[1]}',
                            text_color=COR_CYANO,
                            text_center_pos=SCORE_POS['Title']
                            )

            text = 'Player - entre com seu nome (4 letras):'

            self.score_text(text_size=20, text=text, text_color=COR_BRANCA,
                            text_center_pos=SCORE_POS['Entername'])

            # EVENTOS DENTRO DO SCORE
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(nome_reg) == 4:
                        db_prox.save({'nome': nome_reg,
                                      'score_mago': placar_mago_ghost[0],
                                      'score_ghost': placar_mago_ghost[1]})
                        self.show_score()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        nome_reg = nome_reg[:-1]
                    else:
                        if len(nome_reg) < 4:
                            nome_reg += event.unicode           

            # Escrever o texto na tela
            self.score_text(text_size=20, text=nome_reg, text_color=COR_BRANCA,
                            text_center_pos=SCORE_POS['Label'])
            pygame.display.flip()

    def show_score(self):
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(text_size=35, text='TOP 5 SCORE',
                        text_color=COR_VERDE,
                        text_center_pos=SCORE_POS['Cab'])

        self.score_text(text_size=20, text='PLAYER        MAGO       FANTASMA',
                        text_color=COR_AMARELO,
                        text_center_pos=SCORE_POS['Pontos'])

        db_prox = DBproxy('./Uninter/Linguagem_programacao'
                          '/Trabalho/fantasmas')
        list_score = db_prox.select_top5()
        db_prox.close()

        # Imprime os textos para divulgar score
        for p in list_score:
            id, nome, score_mago, score_ghost = p
            self.score_text(text_size=20, text=f'{nome}             {score_mago}            {score_ghost}',
                            text_color=COR_LARANJA,
                            text_center_pos=SCORE_POS[list_score.index(p)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple,
                   text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",
                                              size=text_size)
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
