from django.contrib import admin

from .models import Novo, Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'email', 'profissional', 'joindate', 'slug', 'criado', 'modificado', 'ativo')


@admin.register(Novo)
class NovoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'email', 'endereco', 'slug')