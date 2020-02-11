from django.db import models

# Create your models here.
class Avaliacoes(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True,blank=True)
    nota = models.DecimalField()
    data = models.DateField(auto_now_add=True)

