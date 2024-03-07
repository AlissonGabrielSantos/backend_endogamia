from django.db import models


class Pelagem(models.Model):
    id_pelagem = models.AutoField(primary_key=True)
    nome_pelagem = models.CharField(max_length=50, null=False)
    active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.nome_pelagem

    class Meta:
        verbose_name = "Pelagem"
        verbose_name_plural = "Pelagens"
