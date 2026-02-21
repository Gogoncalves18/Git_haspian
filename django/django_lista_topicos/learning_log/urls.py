"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin  # Importa o painel admin do django
from django.urls import path  # Indica o caminho da rota
from django.urls import include  # Redireciona para outra URL do app
# sai da pasta projeto e vai para url do APP

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Learning_LOGS.urls')),
]
# Quando entro no site/admin, ele desvia para tela Admin do Django
# Quando for '', é o site origem do django
# Funcao include está direcionando para a URL da app "Learning_LOGS"
