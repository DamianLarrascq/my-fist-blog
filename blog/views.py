from django.shortcuts import render
from .models import Articulo, Tela, ArticuloUsaTela

# Create your views here.

def articulo_completo(request):
    articulo = Articulo.objects.all()
    return render (request, 'articulos.html', {'articulo': articulo})


def articulos_detalle(request):
    articulo = Articulo.objects.all()
    articulousatela = ArticuloUsaTela.objects.all()
    return render (request, 'articulo_detalle.html', {'articulo': articulo})
