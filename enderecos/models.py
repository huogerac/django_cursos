from django.db import models


# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=128)
    bairro = models.CharField(max_length=64, null=False, blank=False)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=2)
