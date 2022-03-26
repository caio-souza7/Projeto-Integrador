from django.db import models


# Create your models here.

class Login(models.Model):
    usuario = models.charField(max_lenght=15)
    senha = models.Charfield(max_lenght=30)

    def __strf__(self):
        return self.usuario
