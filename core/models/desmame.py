from django.db import models
from core.models import animal


class Desmame(models.Model):


    animal = models.OneToOneField(
        "Animal",
        on_delete=models.CASCADE,
        null=False,
        related_name="animal_desmame",
        primary_key=True,
    )
    data_desmame = models.DateField(default="31/12/2000")
    peso_desmame = models.FloatField(null=True, default=1)

    def __str__(self):
        return self.animal.numero_animal

    class Meta:
        verbose_name = "Desmame"
        verbose_name_plural = "Desmames"
