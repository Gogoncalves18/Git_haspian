from django.urls import path  # Indica o caminho da rota
from . import views  # da mesma pasta que este arquivo esta
# ele importa views

urlpatterns = [
    path('', views.index),
]
# Quando for '', é o site origem do django
# Dentro de VIEWS eu terei uma funcao que executará algo e encaminhará
# uma requisicao para o html
