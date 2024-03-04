from django.db import models

class CategoriaRegistro(models.Model):
    id_categoria_registro = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=10)
    
    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = "Categoria de Registro"
        verbose_name_plural = "Categorias de Registro"