from django.db import models
from django.utils import timezone

# Create your models here.

NIVEIS_ACESSO = (
    ("PESQUISADOR", "Pesquisador"),
    ("ENGENHEIRO", "Engenheiro"),
    ("ADMIN_SEGURANCA", "Especialista de Segurança"),
    ("GERENTE", "Gerente"),
    ("SUPERVISOR", "Supervisor"),
    ("FUNCIONARIO", "Funcionário"),
    ("OUTRO", "Outro"),
)

class Area(models.Model):
    setor = models.CharField(max_length=100)
    niveis_acesso = models.CharField(max_length=15, choices=NIVEIS_ACESSO)
    localidade = models.CharField(max_length=255)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.setor

class Recurso(models.Model):
    descricao = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField()
    situacao = models.CharField(max_length=10, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])

    def __str__(self):
        return self.descricao
