from django.contrib import admin
from .models import Produto
from .models import Variacao
from produto import models

class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]

# Registro dos modelos.
admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
