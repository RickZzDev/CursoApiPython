# Generated by Django 3.0.3 on 2020-02-11 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0002_auto_20200211_1000'),
        ('pontos_turisticos', '0002_auto_20200211_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.Atracoes'),
        ),
    ]
