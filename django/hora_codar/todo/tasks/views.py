# Etapa 1 deste arquivo
from django.shortcuts import render
from django.http import HttpResponse

# Etapa 2 deste arquivo
# importar a Class Task para este arquivo para injetar no html os dados do
# BD, as tarefas criadas na tabela tasks do BD
from . models import Task
# Importacao deste modulo serve para validar a ausencia de pagina
from django.shortcuts import get_object_or_404

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
    # Aqui dentro antes de renderizar na tela do html, vamos ler os dados do BD
    # Atraves da funcao do django trazendo os objects que sao instancias da tab
    tasks = Task.objects.all()
    # Assim passamos as tarefas para o html
    return render(request, 'tasks/list.html', {'tasks': tasks})


# Funcao para montar os detalhes de cada lista de tarefa
def taskView(request, id):
    # get_list_or_404() e uma funcao do Django que busca os dados no BD, se
    # nao vier nada, a funcao apresenta pagina 404, se ela vier, eu apresento
    # pego o id para identificar a tarefa e passamos ela para o html
    # 'tasks/task.html'
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def yourName(request, name):
    # Neste caso abaixo eu recebo um argumento e passo
    # ele dentro de chaves para o render jogar no
    # 'tasks/yourname.html', no html recebo a variavel
    # em {{}} dupla, a palavra 'name' é a variavel
    # que recebo da url e jogo no html
    return render(request, 'tasks/yourname.html', {'name': name})
