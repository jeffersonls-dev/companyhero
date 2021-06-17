from django.db import models
from django.contrib.auth.models import User
from apps.empresa.models import Empresa

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ManyToManyField(Empresa)

    def __str__(self):
        return self.nome