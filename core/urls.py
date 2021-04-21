from os import name
from django.urls import path

from .views import index, novo, produto
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('novo/', novo, name='novo'),
    path('resultados/', views.showresults, name='resultados'),
    path('resultadofunc/', views.showresults1, name='resultadosfunc')
]