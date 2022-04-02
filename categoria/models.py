from django.db import models


# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.categoria
