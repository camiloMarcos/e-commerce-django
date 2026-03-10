from django.db import models
from django.contrib.auth.models import User

import pedido

# class Pedido.
class Pedido(models.Model):
        usuario = models.ForeignKey (User, on_delete=models.CASCADE)
        total = models.FloatField ()
        status = models.CharField (
            default = "C",    
            max_length = 1,
            choices = (
                ('A', 'Aprovado'),
                ('C', 'Criado'),
                ('R', 'Reprovado'),
                ('P', 'Pendente'),
                ('E', 'Enviado'),
                ('F', 'Finalizado'),
            )
        )

        def __str__(self):
                return f'Pedido Nº.{self.pk}' #'- {self.usuario.username}'


class ItemPedido(models.Model):
        pedido = models.ForeignKey (Pedido, on_delete=models.CASCADE)
        nomeProduto = models.CharField (max_length=80)
        produto_id = models.PositiveIntegerField ()
        nomeVariacao = models.CharField (max_length=80)
        variacao_id = models.PositiveIntegerField ()
        preco = models.FloatField ()
        preco_promocional = models.FloatField ()
        quantidade = models.PositiveIntegerField ()
        imagem = models.CharField (max_length=2000)

        def __str__(self):
               return f'Item do {self.pedido} Nº.{self.pk}' #'- {self.usuario.username}'
        
        class Meta:
                verbose_name = 'Item do Pedido'
                verbose_name_plural = 'Itens do Pedido'