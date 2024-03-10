from django.db import models
from core.models import animal


class Vaca(models.Model):
    SITUACAO_VACA_CHOICES = {
        "VA": "Vazia",
        "EX": "Exposta",
        "PR": "Prenhe",
        "VP": "Vazia com cria ao pé",
        "EP": "Exposta com cria ao pé",
        "PP": "Prenhe com cria ao pé",
    }

    CATEGORIA_VACA_CHOICES = {
        "NU": "Nulípara",
        "PR": "Primípara",
        "SU": "Secundípara",
        "MU": "Multípara",
    }

    animal = models.OneToOneField("Animal", on_delete=models.CASCADE, null=False, related_name="animal_vaca", primary_key=True)
    situacao_vaca = models.CharField(max_length=2, choices=SITUACAO_VACA_CHOICES, null=True)
    data_primeiro_parto = models.DateField(null=True)
    data_ultimo_parto = models.DateField(null=True)
    quantidade_partos = models.IntegerField(null=True)
    

    active = models.BooleanField(default=True, null=False)
    

    def __str__(self):
        return self.animal

    class Meta:
        verbose_name = "Vaca"
        verbose_name_plural = "Vaca"