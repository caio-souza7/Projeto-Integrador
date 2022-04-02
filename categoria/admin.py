from django.contrib import admin

# Register your models here.
from categoria.models import Categoria


class detCategoria(admin.ModelAdmin):
    list_display = ("id", "categoria")


admin.site.register(Categoria, detCategoria)
