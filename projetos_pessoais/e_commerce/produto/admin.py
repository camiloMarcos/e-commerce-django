from django.contrib import admin
from .models import Produto
from .models import Variacao
from produto import models

# Registro dos modelos.
admin.site.register(models.Produto)
admin.site.register(models.Variacao)
