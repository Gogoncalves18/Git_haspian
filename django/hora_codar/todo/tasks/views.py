# Etapa 1 deste arquivo
from django.shortcuts import render
from django.http import HttpResponse

# Etapa 2 deste arquivo
# importar a Class Task para este arquivo para injetar no html os dados do
# BD, as tarefas criadas na tabela tasks do BD
from . models import Task
# Importacao deste modulo serve para validar a ausencia de pagina
from django.shortcuts import get_object_or_404

# Etapa 3 deste arquivo
# importo de .forms a funcao do formulario para usar na def NewTask(request)
from .forms import TaskForm

# Etapa 4 deste arquivo
# Importacao de redirecionamento de paginas
from django.shortcuts import redirect

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


def NewTask(request):
    '''
    Fucao para adicionar nova task no sistema
    '''
    # Valido se a req e uma consulta ou um post
    if request.method == 'POST':
        # carrego o que foi enviado do form
        form = TaskForm(request.POST)
        # Valido se o form e valido para prosseguir
        if form.is_valid():
            # Salva os dados preenchido no form, com o paramt
            # (commit=False) ele espera o processo de insercao ate
            # definirmos salvar
            task = form.save(commit=False)
            # Pego o campo "done" e transformo em "doing", este campo
            # esta em models.py na class Task que e herdada pelo forms
            # na class TaskForm(forms.ModelForm)
            task.done = "2"
            task.save()
            # Apos executar tudo eu redireciono a pagina para a raiz
            return redirect('/')
    else:
        # Aqui eu instacio a funcao TaskForm() que esta em forms.py
        # para chamar meu formulario.
        form = TaskForm()
        # Apos renderizamos ela fazendo um request para o template html e
        # envio o parametro com o formulario todo para o template
        return render(request, 'tasks/addtask.html', {'form': form})


# Funcao para editar as task, como sempre preciso receber um request e
# no URL.PY tambem estou enviando um arg para ela, um ID
def editTask(request, id):
    # Se ele não vier vazio, eu instancio um model e o id que recebo como pk
    task = get_object_or_404(Task, pk=id)
    # Intancio em um form e deixo ele pre preenchido passando como instance
    # a task
    form = TaskForm(instance=task)
    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)
        # Valido se o form que foi preenchido esta valido, como 
        # tipo de campo, tamanho de campo, os campos
        if (form.is_valid()):
            task.save()
            return redirect('/')
        else:
            # Se der erro, volto para a mesma tarefa que iria editar
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        # Se eu nao recebo uma req POST, entao renderizo na tela para o req
        # o ./edittask.html entregando para ele o FORM e a TASK
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})


def tasklist(request):
    # Aqui dentro antes de renderizar na tela do html, vamos ler os dados do BD
    # Atraves da funcao do django trazendo os objects que sao instancias da tab
    # "order_by('-create_at')" e a maneira de pedir para o django ordenar pelo
    # campo que criamos na tabela create_at e o sinal de "-" diz a ela para
    # fazer do mais novo para o mais antigo
    tasks = Task.objects.all().order_by('-created_at')
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
