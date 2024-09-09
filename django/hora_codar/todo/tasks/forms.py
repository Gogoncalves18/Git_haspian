from django import forms
# importacao da class que criamos os campos no models
from .models import Task


# Definicao do padrao de formulario no django
class TaskForm(forms.ModelForm):
    # classe parece obrigatoria
    class Meta:
        # instancio os dados da class anterios
        model = Task
        # campos que vou trazer da class Task, no front end
        fields = ('title', 'description')
