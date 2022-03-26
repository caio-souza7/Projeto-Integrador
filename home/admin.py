from django.contrib import admin

# Register your models here.
from home.models import Login


@admin.register(Login)
class detLogin(admin.ModelAdmin):
    list_display = ('usuario', 'senha')
