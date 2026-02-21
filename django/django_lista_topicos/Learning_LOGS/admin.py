from django.contrib import admin
# Necessario importar o model para aparecer na URL do admin
from Learning_LOGS.models import Topic, Entry

# Register your models here.
# Registro para a area administrativa do djanco, defino que 
# eu possuo uma tabela Topic no BD
admin.site.register(Topic)
admin.site.register(Entry)
