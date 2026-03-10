from django.db import models

# Create your models here.
class PerfilUsuario(models.Model):
        user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
        idade = models.IntegerField()
        data_nascimento = models.DateField()
        cpf = models.CharField (max_length=14)
        endereco = models.CharField (max_length=200)
        numero = models.CharField (max_length=10)
        complemento = models.CharField (max_length=100)
        bairro = models.CharField (max_length=100)
        cep = models.CharField (max_length=9)
        cidade = models.CharField (max_length=100)
        estado = models.CharField (
                max_length = 2,
                choices = [
                    ('AC', 'Acre'),
                    ('AL', 'Alagoas'),
                    ('AP', 'Amapá'),
                    ('AM', 'Amazonas'),
                    ('BA', 'Bahia'),
                    ('CE', 'Ceará'),
                    ('DF', 'Distrito Federal'),
                    ('ES', 'Espírito Santo'),
                    ('GO', 'Goiás'),
                    ('MA', 'Maranhão'),
                    ('MT', 'Mato Grosso'),
                    ('MS', 'Mato Grosso do Sul'),
                    ('MG', 'Minas Gerais'),
                    ('PA', 'Pará'),
                    ('PB', 'Paraíba'),
                    ('PR', 'Paraná'),
                    ('PE', 'Pernambuco'),
                    ('PI', 'Piauí'),
                    ('RJ', 'Rio de Janeiro'),
                    ('RN', 'Rio Grande do Norte'),
                    ('RS', 'Rio Grande do Sul'),
                    ('RO', 'Rondônia'),
                    ('RR', 'Roraima'),
                    ('SC', 'Santa Catarina'),
                    ('SP', 'São Paulo'),
                    ('SE', 'Sergipe'),
                    ('TO', 'Tocantins'),
                ]
        )