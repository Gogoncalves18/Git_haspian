from django.db import models

# Create your models here. Este arquivo e responsavel
# pela criacao de campos que irao abastecer o sql via
# comando migration. Apos definir o models, precisamos
# executar no terminal o comando "python .\manage.py makemigrations"
# que ira criar um arquivo na pasta migrations dentro do app em questao
# este arquivo possui as instrucoes sql.
# Apos precisamos executar o cmd "python .\manage.py migrate" que
# ira migrar todos os modulos pendentes no django para o BD.
# Apos isto ele tem a area adm, porem sem user, para criar o user:
# "python .\manage.py createsuperuser"
# entra com o nome e email e senha para criar o user no BD
# Apos dentro do arquivo "ADMIN.py" que esta dentro do app em questao
# eu preciso cadastrar todos os models class que eu quero ter acesso
# no modo adm.


class Task(models.Model):
    # Variavel para alimentar um subselect dentro do charfield,
    # ela recebe uma tupla com valor e descricao
    STATUS = (
        ('1', "doing"),
        ('2', "Done"),
    )

    # Charfield de models e o tipo do campo que tem uma definicao
    # de comprimento para ser trabalhado no sql pelo migration,
    # aqui ja estamos formatando a tabela
    title = models.CharField(max_length=255)
    # TextField e uma funcao sem parametro, ela ja define uma
    # comprimento infinito para o texto
    description = models.TextField()
    # Este campo servira para definir se a tarefa ja foi realizada
    # neste caso o tamanho do campo sera 1 (feito e fazendo), em
    # casos que eu quero um campo com opcoes, posso usar um parametro
    # da funcao Charfield que permite um especie de select em uma variavel
    # criando opcoes em formato de tupla
    done = models.CharField(
        max_length=1, choices=STATUS,
        )
    # Este 2 campos e uma boa pratica pois controlaremos o quando o registro
    # foi criado e o quando foi atualizado. A opcao da funcao DateTimeField
    # define que o campo sera de data/hora completa e o paramentro
    # Auto_now=True define que ele sera de preenchimento automatico
    # na atualizacao do dado
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # No ambiente admin, para eu nao ver os objetos do BD como objetos, posso
    # usar a funcao do django abaixo para ele converter a informacao em uma
    # propriedade do objeto.

    def __str__(self):
        return self.title
