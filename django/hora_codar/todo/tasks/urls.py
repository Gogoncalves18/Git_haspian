"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


# Funcao path define a url e a views do app
# O olamundo precisa ser criado no arquivo de views.py
# primeiro parametro e o nome do html e o segundo e
# a view. E ainda ha o 'name' que e um apelido para a pagina.
# Toda view precisa de uma funcao que recebe um request em views.py
# e sempre retorna algo.
urlpatterns = [
    # Nesta linha ele abre em http://127.0.0.1:8000/ola xx mundo/
    path('ola xx mundo/', views.olamundo),
    # Nesta linha ele abre na janela raiz em http://127.0.0.1:8000/
    path('', views.tasklist, name='task-list'),
    # url para conectar html 'newtask/' a funcao da view NewTask
    path('newtask/', views.NewTask, name='new-task'),
    # Url para editar task, nela eu passo um arg ID que e representado
    # por <int:id>
    path('edit/<int:id>', views.editTask, name="edit-task"),
    # Passar dados via html, olhar o views.py, sendo o <str:name>
    # a maneira de passar parametros pela url.
    path('yourname/<str:name>', views.yourName, name='yname'),
    path('task/<int:id>', views.taskView, name='task-view'),
]
# <str:name>
