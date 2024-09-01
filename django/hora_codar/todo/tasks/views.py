from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Dentro do response é o que e impresso na tela
def olamundo(request):
    return HttpResponse('ola mundo!!!!')


# Nas funcoes da view eu posso renderizar um html,
# recebo a request do django e devolvo um html,
# para isto funcionar preciso criar uma pasta
# templates dentro da raiz do app tasks, dentro
# dela preciso criar outra pasta com o nome
# do app. Meu
# template neste caso e o 'tasks/list.html'

def tasklist(request):
    return render(request, 'tasks/list.html')


def yourName(request, name):
    # Neste caso abaixo eu recebo um argumento e passo
    # ele dentro de chaves para o render jogar no
    # 'tasks/yourname.html', no html recebo a variavel
    # em {{}} dupla, a palavra 'name' é a variavel
    # que recebo da url e jogo no html
    return render(request, 'tasks/yourname.html', {'name': name})
