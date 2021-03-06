# Generated by Django 3.0.3 on 2020-02-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('comentarios', '0002_comentarios_comentario'),
        ('pontos_turisticos', '0003_pontosturisticos_atracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacoes'),
        ),
        migrations.AddField(
            model_name='pontosturisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentarios'),
        ),
    ]
