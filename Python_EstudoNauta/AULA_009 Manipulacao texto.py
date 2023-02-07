#fatiamento de STRINGS
fr = 'Curso em video python'
#-----012345678901234567890
print (fr[9]) #pega a posicao 9 da frase, , resposta sera v
print (fr[9:13]) #pega parte da palavra video que esta entre posicao 9, 10,11,12, resposta sera vide
print (fr[9:20:3]) #neste fatiamento ele vai de 9 a 20 pulando de 3 em 3, resposta sera veph
print (fr[:7]) #comeca do ponto zero e vai ate posicao 7, resposta sera Curso e
print (len(fr)) #comprimento da STR
print (fr.count('o')) #conta quantas vezes ha O na frase, resposta sera 3
print (fr.count('o', 0, 13)) # conta quanto O existe no fatiamento 0 a 13, , resposta sera 1
print (fr.find('deo')) #mostra onde comeca a palavra DEO, , resposta sera pos 11
print (fr.find('teta')) #quando ele nao encontra, ele retorna o vlr -1 pois nao ha esta posicao
print ('Curso' in fr) #retorna valor True se a palavra possui na frase
print (fr.replace('python','android')) #substitui uma palavra por outra nao na frase mas na saida dela
print (fr.upper()) #troca de minuscula para maiuscula
print (fr.capitalize()) #so o inicio da frase fica maiuscula
print (fr.title()) #todas as primeiras letras ficam maiusculas
print (fr.strip()) #remove os espacos do inicio de final se tiver espacos. Se colocar rstrip ao qual removo os espacos da direita
print (fr.split()) #cria uma lista com cada palavra da frase. ' '.join(fr) juntaria a lista em uma frase com o espaco
