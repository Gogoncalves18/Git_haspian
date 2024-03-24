# Programa que leia nome e media de um aluno
# Guardando a situacao dele aprovado ou Reprovado
# sobre media 6
# No final mostre o conteudo na tela de forma
# bruta e construida

aluno = {'nome': '0', 'media': '0', 'sit': '0'}
aluno['nome'] = input('\nDigite o nome do aluno: ')
aluno['media'] = int(input('\nDigite a media dele: '))
if aluno['media'] >= 6:
    aluno['sit'] = 'APROVADO'
else:
    aluno['sit'] = 'REPROVADO'
print('-*-'*40)
print(f'\nCadastro do Aluno => {aluno}')
print('-*-'*40)
print(f'''\nO aluno {aluno["nome"]} com Media {aluno["media"]}
está {aluno["sit"]}!''')
