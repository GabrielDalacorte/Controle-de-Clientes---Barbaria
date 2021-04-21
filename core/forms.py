from django import contrib, forms
from django.contrib.admin import widgets
from django.core.mail.message import EmailMessage

from django.db.models import signals
from django.template.defaultfilters import slugify

from .models import Produto, Novo


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'telefone', 'email', 'profissional', 'joindate']


class NovoModelForm(forms.ModelForm):
    class Meta:
        model = Novo
        fields = ['nome', 'telefone', 'email', 'endereco']