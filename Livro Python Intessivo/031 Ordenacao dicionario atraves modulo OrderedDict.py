from collections import OrderedDict
from operator import itemgetter
fav_lang = {}
fav_lang['Val'] = 'C#'
fav_lang['Gus'] = 'Python'
fav_lang['Teixeira'] = 'Ruby'
fav_lang['Andre'] = 'Google R'
fav_lang['Petra'] = 'C#'

print('DICIONARIO FORA DE ORDEM: ')
print(fav_lang)
print(F'\nDEFINIÇÃO DE UMA LISTA PARA CONVERTER O DICIONARIO EM LISTA E ENTÃO APLICAR O ITEMGETTER PARA ORDENAR')
pessoas_lang = []
pessoas_lang = sorted(fav_lang.items()) #Neste caso ele pega a primeira Key e ordena por ela, ao contrario do itemgetter que eu escolho o que quero ordenar
print(pessoas_lang)
pessoas_lang = sorted(fav_lang.items(), key=itemgetter(1), reverse=False) #AQUI A CHAVE QUE ORDENARÁ É A POSIÇÃO 0 QUE SERIA A CHAVE DO DICT OU POS 1 QUE É O VALOR DO DICT
print(pessoas_lang)

print(F'\nORDENAÇÃO PELO MODULO DO PYTHON DE ORDENAR DICIONARIO')

fav_lang2 = OrderedDict() #Este mmodulo garante que a posição de inserção dos dados serão sempre respeitados
fav_lang2['Val'] = 'C#'
fav_lang2['Gus'] = 'Python'
fav_lang2['Teixeira'] = 'Ruby'
fav_lang2['Andre'] = 'Google R'
fav_lang2['Petra'] = 'C#'

print(fav_lang2)