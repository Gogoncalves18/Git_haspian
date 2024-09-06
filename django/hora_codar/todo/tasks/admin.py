from django.contrib import admin

# Register your models here.
# Esta linha embaixo eu preciso importar a classe criada dentro de models.
from .models import Task

# Funcao do Django para registrar a Class criada em models
admin.site.register(Task)
