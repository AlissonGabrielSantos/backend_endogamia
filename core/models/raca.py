from django.db import models


class Raca(models.Model):
    id_raca = models.AutoField(primary_key=True)
    nome_raca = models.CharField(max_length=50)
    active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.nome_raca

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"
