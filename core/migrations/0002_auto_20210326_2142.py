# Generated by Django 3.1.7 on 2021-03-27 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('email', models.EmailField(max_length=120, verbose_name='E-mail')),
                ('endereco', models.CharField(max_length=200, verbose_name='Endereço')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='produto',
            name='joindate',
            field=models.DateField(verbose_name='Data do Atendimento'),
        ),
    ]
