from django.db import models

class Organizacao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cnpj = models.CharField(max_length=20)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Organização"
        verbose_name_plural = "Organizações"