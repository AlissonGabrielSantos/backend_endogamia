from django.db import models

class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    organizacao = models.ForeignKey("Organizacao", on_delete=models.CASCADE, related_name="organizacao_lote", default=1)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"