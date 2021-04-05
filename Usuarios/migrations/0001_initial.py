# Generated by Django 3.0 on 2021-04-05 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome completo:')),
                ('pais', models.CharField(max_length=194, verbose_name='País')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado:')),
                ('cidade', models.CharField(max_length=194, verbose_name='Cidade:')),
                ('bairro', models.CharField(max_length=194, verbose_name='Bairro:')),
                ('logradouro', models.CharField(max_length=194, verbose_name='Logradouro:')),
                ('numero_da_casa', models.CharField(max_length=194, verbose_name='Número da residencia:')),
                ('CNPJ', models.CharField(max_length=194, unique=True, verbose_name='CNPJ da empresa:')),
                ('inscricao_estadual', models.CharField(max_length=194, unique=True, verbose_name='Inscrição estadual da empresa:')),
                ('telefone', models.CharField(blank=True, max_length=194, null=True, verbose_name='Telefone da residencia:')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro')),
            ],
            options={
                'verbose_name': 'Empresa:',
                'verbose_name_plural': 'Empresas:',
                'db_table': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=194, verbose_name='Nome completo:')),
                ('naturalidade', models.CharField(max_length=194, verbose_name='Naturalidade')),
                ('pais', models.CharField(max_length=194, verbose_name='País')),
                ('escolaridade', models.CharField(choices=[('EFI', 'Ensino fundamental incompleto'), ('EFC', 'Ensino fundamental completo'), ('EMI', 'Ensino médio incompleto'), ('EMC', 'Ensino médio completo'), ('ESI', 'Ensino superior incompleto'), ('ESC', 'Ensino superior completo')], max_length=30, verbose_name='Escolaridade:')),
                ('status', models.CharField(choices=[('FEMININO', 'Feminino'), ('MASCULINO', 'Masculino'), ('OUTRO', 'Outro')], max_length=10, verbose_name='Genero')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail:')),
                ('telefone_celular', models.CharField(max_length=19, verbose_name='Número de telefone')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF:')),
                ('nascimento', models.DateField(max_length=10, verbose_name='Data de nascimento:')),
                ('estado_civil', models.CharField(choices=[('SOLTEIRO(A)', 'Solteiro(a)'), ('CASADO(A)', 'Casado(a)'), ('DIVORCIADO(A)', 'Divorciado(a)')], max_length=40, verbose_name='Estado civil:')),
                ('profissao', models.CharField(max_length=194, verbose_name='Profissão:')),
                ('cep', models.CharField(max_length=194, verbose_name='CEP:')),
                ('estado', models.CharField(max_length=30, verbose_name='Estado:')),
                ('cidade', models.CharField(max_length=194, verbose_name='Cidade:')),
                ('bairro', models.CharField(max_length=194, verbose_name='Bairro:')),
                ('logradouro', models.CharField(max_length=194, verbose_name='Logradouro::')),
                ('numero', models.CharField(max_length=194, verbose_name='Número da residencia:')),
                ('telefone', models.CharField(blank=True, max_length=194, null=True, verbose_name='Telefone da residencia:')),
                ('data_de_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data do cadastro')),
            ],
            options={
                'verbose_name': 'Pessoa:',
                'verbose_name_plural': 'Pessoas:',
            },
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Empresa')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Pessoa')),
            ],
            options={
                'verbose_name': 'Vendedor:',
                'verbose_name_plural': 'Vendedores:',
                'db_table': 'vendedor',
            },
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.Pessoa')),
            ],
            options={
                'verbose_name': 'Gerente:',
                'verbose_name_plural': 'Gerentes:',
                'db_table': 'Gerente',
            },
        ),
    ]
