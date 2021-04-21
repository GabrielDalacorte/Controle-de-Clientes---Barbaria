# Generated by Django 3.1.7 on 2021-03-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(blank=True, max_length=11, null=True, verbose_name='Nº telefone celular')),
                ('email', models.EmailField(max_length=120, verbose_name='E-mail')),
                ('profissional', models.CharField(choices=[('Leon', 'Leon'), ('Gabriel', 'Gabriel'), ('Nenhuma das opções', 'Nenhuma das opções')], max_length=30)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
                ('joindate', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]