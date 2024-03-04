from django.db import models
from core.models import raca, pelagem, lote


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
    
    id_animal = models.CharField(max_length=7, primary_key=True)
    data_nascimento = models.DateField(default="2000-12-31")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    raca = models.ForeignKey("Raca", on_delete=models.CASCADE, related_name="raca_animal")
    animal_ativo = models.BooleanField(default=True)
    atividade = models.CharField(max_length=1, choices=ATIVIDADE_CHOICES, default="C")
    categoria = models.CharField(max_length=2, choices=CATEGORIA_CHOICES, default="BE")
    pelagem = models.ForeignKey("Pelagem", on_delete=models.CASCADE, related_name="pelagem_animal")
    lote = models.ForeignKey("Lote", on_delete=models.CASCADE, related_name="lote_animal", default=1)

    def __str__(self):
        return self.id_animal

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"
