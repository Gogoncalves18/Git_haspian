'''Crie um programa que tenha uma funcao chamada votos que receberá
como parametro o ano de nascimento de uma pessoa. A funcao deve retornar
um valor literal indicando se uma pessoa tem voto negado, opcional ou
obrigatorio
'''
from datetime import date #utilizado para calculo de idade


def votos(ano): #funcao que recebe o ano de nascimento
    ano_atual = date.today().year #calculo do ano atual
    if ano_atual - ano > 18 and ano_atual - ano <= 60: #retorno da funcao para quem deve voltar
        return f'\nSeu voto é obrigatorio !'
    elif ano_atual - ano > 60: #retorno da funcao para que não vota mais
        return f'\nTu é velho, vai dormir!!!'
    elif ano_atual - ano < 18: #retorno para quem é menor de idade
        return f'\nVai aprender a se limpar direiro pirralho!'


#PROGRAMA PRINCIPAL
print(votos(int(input(f'\nEm que ano vc nasceu: ')))) #Chamada da funcao com input para o terminal
