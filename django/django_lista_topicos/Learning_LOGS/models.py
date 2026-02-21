from django.db import models

# Create your models here.
# Aqui criamos a classe que irá transacionar com o BD e ela sempre
# herda de models.Model


class Topic(models.Model):
    """Assuntos que o usuário está inserindo"""
    # Embaixo as colunas do banco com a tipagem de dados
    text = models.CharField(max_length=200)
    # Preenchimento automatico de data ao ocorrer a insercao
    date_added = models.DateTimeField(auto_now_add=True)

    # funcao para mostrar no painel administrativo de uma forma mais formatada

    def __str__(self):
        """Devolve uma representacao do modelo do BD"""
        return self.text

# Criacao de uma tabela que será os assuntos de cada topico em "Topic"
# Sendo assim ele terá uma relacao de (1to*)


class Entry(models.Model):
    # Entry é o nome da tabela
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # esta funcao acima serve para travar para cada PK desta tabela, uma 
    # FK da tabela Topic. Importante, on_delete é obrigatório, a opcao
    # CASCADE faz com que se um topico de Topic for deletado, ela deleta o
    # assuntos dentro dela.
    text = models.TextField()  # Campo de texto
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Esta classe dentro da classe ENTRY apenas passa para o django
        # que quando ele quiser usar o nome da tabela ENTRY no plural
        # é para ele usar o termo: "ENTRIES"
        verbose_name_plural = 'ENTRIES'

    def __str__(self):
        """Devolve uma representacao do modelo do BD"""
        # Este esta funcao, ele estava mostrando apenas o nome do objeto
        return self.text[:20] + '...'
