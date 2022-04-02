from django.db import models

# Create your models here.
from categoria.models import Categoria


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=50, default=None)
    descricao = models.CharField(max_length=200, default=None)
    fornecedor = models.CharField(max_length=50)
    preco = models.DecimalField(decimal_places=2, max_digits=10, default=None)
    quantidade = models.IntegerField()
    foto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nome + '' + str(self.categoria)
        # return self.nome1

