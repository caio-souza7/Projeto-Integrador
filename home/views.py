from django.shortcuts import render

# Create your views here.
from categoria.models import Categoria
from produto.models import Produto


def index(request):
    cosmeticos = Produto.objects.order_by('id').filter(categoria_id=1)
    remedios = Produto.objects.order_by('id').filter(categoria_id=2)
    return render(request, 'home/index.html', {'cosmeticos': cosmeticos, 'remedios': remedios})


def desenvolvedor(request):
    return render(request, 'home/desenvolvedor.html')


def contato(request):
    return render(request, 'home/contato.html')
