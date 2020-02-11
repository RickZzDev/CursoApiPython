from django.db import models

# Create your models here.
class Atracoes(models.Model):
    nome = models.CharField(max_length=80)
    descricao = models.TextField()
    hora = models.IntegerField()
    min_idade = models.IntegerField()
  

    def __str__(self):
        return self.nome