from django.db import models


# Create your models here.

class Produto(models.Model):
    idProduto = models.IntegerField()
    nomeProduto = models.CharField(max_length=50)
    fornecedor = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __strf__(self):
        return self.idProduto
