# Generated by Django 3.0.3 on 2020-02-12 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('pontos_turisticos', '0004_auto_20200212_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='endereco.Endereco'),
            preserve_default=False,
        ),
    ]