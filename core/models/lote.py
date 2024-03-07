from django.db import models
from core.models import animal, subdivisao
class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    touro = models.ForeignKey("Animal", on_delete=models.CASCADE, related_name="touro_lote", default=1)
    nome_lote = models.CharField(max_length=100)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    organizacao = models.ForeignKey("Subdivisao", on_delete=models.CASCADE, related_name="subdivisao_lote", default=1)
    vaca = models.ManyToManyField("Animal", related_name="vaca_lote")
    active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.nome_lote

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"