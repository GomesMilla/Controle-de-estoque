# Generated by Django 3.0 on 2021-04-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtostransacao',
            name='qtd_de_produtos',
            field=models.FloatField(verbose_name='Quantidade de produto:'),
        ),
    ]
