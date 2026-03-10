from django.db import models
from django.forms import CharField, FloatField, SlugField
from PIL import Image
import os
from django.conf import settings

# models - Produto:
class Produto(models.Model):
            
            nome = models.CharField(max_length=80, default='Produto sem nome')
            descricao_curta = models.TextField(max_length=150)
            descricao_longa = models.TextField(max_length=300)
            imagem = models.ImageField(
                 upload_to='produto/produto_imagens/%y/%m', blank=True, null=True)
            slug = models.SlugField( unique=True, max_length=100)
            preco_marketing = models.FloatField()
            preco_marketing_promocional = models.FloatField(default=0)
            tipo = models.CharField(
                    default='V',
                    max_length=1,
                    choices= (
                        ('V', 'Variação'),
                        ('S', 'Simples'),
                    )
                )




# Redimensiona a imagem para no máximo 'new_width' pixels de largura, mantendo a proporção, e salva com qualidade reduzida
@staticmethod
def resize_image(img, new_width =800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
                img_pil.close()
                return
        
        new_height = round((new_width * original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
                img_full_path,
                optimize=True,
                quality=50 
        )


# Salva o objeto no banco de dados e redimensiona a imagem caso exista            )
def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size=800

        if self.imagem:
                self.resize_image(self.imagem, max_image_size)


# Define como o objeto será exibido em texto (ex: no Django Admin)
def __str__(self):
        return self.nome



class Variacao(models.Model):
        Produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
        nome = models.CharField(max_length=80, blank=True, null=True)
        preco = models.FloatField()
        preco_promocional = models.FloatField(default=0)
        estoque = models.PositiveIntegerField(default=1)

        def __str__(self):
                return self.nome or self.Produto.nome
        
        class Meta:
                verbose_name = 'Variação'
                verbose_name_plural = 'Variações'


