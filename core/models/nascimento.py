from django.db import models
from core.models import animal


class Nascimento(models.Model):
    TAMANHO_CHOICES = {
        "P": "Pequeno",
        "M": "Médio",
        "G": "Grande",
    }

    SITUACAO_CHOICES = {
        "U": "Único",
        "M": "Múltiplo",
        "D": "Defeituoso Único",
        "N": "Defeituoso Múltiplo",
    }

    TIPO_PARTO_CHOICES = {
        "N": "Normal",
        "A": "Assistido",
        "C": "Cirúrguco",
        "M": "Natimorto",
        "F": "Abortado",
    }

    animal = models.OneToOneField(
        "Animal",
        on_delete=models.CASCADE,
        null=False,
        related_name="animal_nascimento",
        primary_key=True,
    )
    tamanho_nascimento = models.CharField(
        max_length=1, choices=TAMANHO_CHOICES, default="M"
    )
    data_nascimento = models.DateField(default="31/12/2000")
    situacao_nascimento = models.CharField(
        max_length=1, choices=SITUACAO_CHOICES, default="U"
    )
    ordem_parto = models.IntegerField(null=True, default=1)
    tipo_parto = models.CharField(max_length=1, choices=TIPO_PARTO_CHOICES, default="N")

    def __str__(self):
        return self.id_nascimento

    class Meta:
        verbose_name = "Nascimento"
        verbose_name_plural = "Nascimentos"
