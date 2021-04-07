# Generated by Django 3.0 on 2021-04-07 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_auto_20210407_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF:'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='logradouro',
            field=models.CharField(max_length=194, verbose_name='Logradouro:'),
        ),
    ]
