from django.db import models
from core.models import animal, lote

class VacaLote(models.Model):
    id_vaca_lote = models.AutoField(primary_key=True)
    lote = models.ForeignKey("Lote", on_delete=models.CASCADE, related_name="lote_vaca", default=1)
    vaca = models.ForeignKey("Animal", on_delete=models.CASCADE, related_name="vaca_lote", default=1)
    data_cadastro = models.DateField(auto_now_add=True)
    data_atualizacao = models.DateField(auto_now=True)
    active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.lote.nome_lote + " - " + self.animal.numero_animal

    class Meta:
        verbose_name = "VacaLote"
        verbose_name_plural = "VacasLotes"