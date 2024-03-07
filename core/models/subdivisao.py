from django.db import models
from core.models import organizacao


class Subdivisao(models.Model):
    id_subdivisao = models.AutoField(primary_key=True)
    nome_subdivisao = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    organizacao = models.ForeignKey("Organizacao", on_delete=models.CASCADE, related_name="organizacao_subdivisao", default=1)
    active = models.BooleanField(default=True, null=False)
    
    def __str__(self):
        return self.nome_subdivisao

    class Meta:
        verbose_name = "Subdivisão"
        verbose_name_plural = "Subdivisões"