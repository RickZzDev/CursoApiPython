from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
# Create your models here
class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    status = models.BooleanField(default=False)
    atracao =   models.ManyToManyField(Atracoes)
    comentarios = models.ManyToManyField(Comentarios)

    def __str__(self):
        return self.nome
