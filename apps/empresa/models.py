from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome da empresa')
    cnpj = models.CharField(max_length=14, help_text='CNPJ da empresa')

    def __str__(self):
        return self.nome
