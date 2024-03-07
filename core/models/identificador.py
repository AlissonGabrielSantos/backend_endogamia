from django.db import models
from core.models import animal, categoria_registro


class Identificador(models.Model):


    animal = models.OneToOneField(
        "Animal",
        on_delete=models.CASCADE,
        null=False,
        related_name="animal_identificador",
        primary_key=True,
    )
    nome_animal = models.CharField(max_length=100, null=True)
    brinco_eletronico = models.CharField(max_length=50, null=True)
    numero_sisbov = models.CharField(max_length=50, null=True)
    data_id_sisbov = models.DateField(null=True)
    data_certificacao_sisbov = models.DateField(null=True)
    registro_nascimento = models.CharField(max_length=50, null=True)
    registro_definitivo = models.CharField(max_length=50, null=True)
    serie = models.CharField(max_length=50, null=True)
    categoria_registro = models.ForeignKey("CategoriaRegistro", on_delete=models.SET_DEFAULT, related_name="categoria_registro_identificador", default=1)
    a12 = models.CharField(max_length=50, null=True)
    serie_paint_cia = models.CharField(max_length=50, null=True)
    active = models.BooleanField(default=True, null=False)


    def __str__(self):
        return self.animal.numero_animal

    class Meta:
        verbose_name = "Identificador"
        verbose_name_plural = "Identificadores"
