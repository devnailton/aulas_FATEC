from django.db import models
from enderecos.models import Endereco
from datetime import date

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=12, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    historico_medico = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
    '''# Método para calcular a idade
    def calcular_idade(self):
        hoje = date.today()
        nascimento = self.data_nascimento
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade'''