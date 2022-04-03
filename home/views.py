from django.shortcuts import render

# Create your views here.
from produto.models import Produto


def index(request):
    dados = Produto.objects.order_by('id')
    return render(request, 'home/index.html', {'dados': dados})
