from django.db import models
from django.db.models.base import Model
from django.db.models.fields import DateField
from stdimage.models import StdImageField
from django import contrib, forms


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
        #db_table = "core_produto"


class Produto(Base):
    Profissional_choices = (
        ("Leon", "Leon"),
        ("Gabriel", "Gabriel"),
        ("Nenhuma das opções", "Nenhuma das opções")
    )
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    email = models.EmailField('E-mail', max_length=120)
    profissional = models.CharField(max_length=30, choices=Profissional_choices, blank=False, null=False)    
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    joindate = models.DateField('Data do Atendimento')
    

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(produto_pre_save, sender=Produto)
#########

class Novo(Base):

    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    email = models.EmailField('E-mail', max_length=120)
    endereco = models.CharField('Endereço', max_length=200)   
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False) 

    def __str__(self):
        return self.nome


def novo_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)


signals.pre_save.connect(novo_pre_save, sender=Novo)



