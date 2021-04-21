# TUDO QUE A GENTE QUISER ENVIAR PARA O SITE

from django.db import models
from django.shortcuts import redirect, render, resolve_url

from django.contrib import messages
from .forms import NovoModelForm, ProdutoModelForm
from django.shortcuts import redirect
from .models import Produto, Novo
# Create your views here.

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto.')
        else:
            form = ProdutoModelForm() #Caso o form nao for post faca isso
        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('index')


def novo(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form2 = NovoModelForm(request.POST, request.FILES)
            if form2.is_valid():

                form2.save()

                messages.success(request, 'Produto salvo com sucesso.')
                form2 = NovoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produto.')
        else:
            form2 = NovoModelForm() #Caso o form nao for post faca isso
        context = {
            'form': form2
        }

        return render(request, 'novo.html', context)
    else:
        return redirect('index')


#############
from .models import Produto


def showresults(request):
    if request.method=="POST":
        fromdate=request.POST.get('fromdate')
        searchresult=Produto.objects.raw("select id, nome, telefone, email, profissional, joindate from core_produto where joindate = '"+fromdate+"' ")
        return render(request, 'resultados.html',{"data":searchresult})
    else:
        displaydata=Produto.objects.all()
        return render(request, 'resultados.html',{"data":displaydata})
        return redirect('index')

#############
from .models import Novo


def showresults1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        searchresult1=Novo.objects.raw("select id, nome, telefone, email, joindate from core_produto where core_produto.profissional = '"+name+"' ")
        return render(request, 'resultadofunc.html',{"func":searchresult1})
    else:
        displaydata=Novo.objects.all()
        return render(request, 'resultadofunc.html',{"func":displaydata})
        return redirect('index')
