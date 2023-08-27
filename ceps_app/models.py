from django.db import models

# Create your models here.
class Ceps(models.Model):
    cep = models.CharField(max_length=8, null=False, blank=False)

class Endereco(models.Model):
    Endereco = models.CharField(max_length=250, null=False, blank=False)

