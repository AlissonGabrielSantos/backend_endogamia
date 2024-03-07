from django.db import models
from core.models import raca, pelagem


class Animal(models.Model):
    SEXO_CHOICES = {
        "M": "Macho",
        "F": "Fêmea",
    }
    
    ATIVIDADE_CHOICES = {
        "C": "Cria",
        "R": "Recria",
        "E": "Engorda",
    }

    CATEGORIA_CHOICES = {
        "BE": "Bezerro",
        "GA": "Garrote",
        "TO": "Touro",
        "BI": "Boi",
        "BA": "Bezerra",
        "NO": "Novilha",
        "VA": "Vaca",
    }
    id_animal = models.AutoField(primary_key=True)
    numero_animal = models.CharField(max_length=7, default="0000000")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=True)
    raca = models.ForeignKey("Raca", on_delete=models.CASCADE, related_name="raca_animal", null=True)
    animal_ativo = models.BooleanField(default=True, null=False)
    atividade = models.CharField(max_length=1, choices=ATIVIDADE_CHOICES, default="C", null=True)
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES, default="BE", null=True)
    pelagem = models.ForeignKey("Pelagem", on_delete=models.CASCADE, related_name="pelagem_animal", null=True)

    def __str__(self):
        return self.numero_animal

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
