from django.db import models


# Create your models here.

class Login(models.Model):
    usuario = models.CharField(max_length=15)
    senha = models.CharField(max_length=30)

    def __strf__(self):
        return self.usuario
