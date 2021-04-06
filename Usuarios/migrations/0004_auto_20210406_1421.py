# Generated by Django 3.0 on 2021-04-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_empresa_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nome',
            field=models.CharField(max_length=194, verbose_name='Nome da empresa:'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='numero_da_casa',
            field=models.CharField(max_length=194, verbose_name='Número da residencia ou complemento:'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=194, null=True, verbose_name='Contato da empresa:'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF:'),
        ),
    ]