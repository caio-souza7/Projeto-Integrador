from django.contrib import admin

# Register your models here.
from produto.models import Produto


class detProduto(admin.ModelAdmin):
    list_display = ("id", "categoria", "nome", "descricao", "fornecedor", "preco", "quantidade", "foto")


admin.site.register(Produto, detProduto)
