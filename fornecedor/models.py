from django.db import models


# Create your models here.
class Fornecedor(models.Model):
    idFornecedor = models.IntegerField()
    nomeFornecedor = models.CharField(max_length=50)
    nomeProduto = models.CharField(max_length=50)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    def __strf__(self):
        return self.idFornecedor
