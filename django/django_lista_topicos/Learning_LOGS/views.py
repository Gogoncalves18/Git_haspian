from django.shortcuts import render

# Create your views here.


def index(request):
    # Aqui há uma requisicao que sera para o browser para entao renderizar
    # respondida
    return render(request, 'learning_LOGS/index.html')
    # Ele pega a requisicao e joga as informacoes de request no arquivo
    # 'learning_LOGS/index.html'
