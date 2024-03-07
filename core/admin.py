from django.contrib import admin
from .models import Animal, CategoriaRegistro, Desmame, Identificador, Lote, Nascimento, Organizacao, Pelagem, Raca, Subdivisao, VacaLote

#admin.site.register(Animal)
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('numero_animal','id_animal')
    search_fields = ('numero_animal','id_animal')
    list_filter = ('numero_animal','id_animal')
    ordering = ('numero_animal','id_animal')


admin.site.register(CategoriaRegistro)
admin.site.register(Desmame)
admin.site.register(Identificador)
admin.site.register(Lote)
admin.site.register(Nascimento)
admin.site.register(Organizacao)
admin.site.register(Pelagem)
admin.site.register(Raca)   
admin.site.register(Subdivisao)
admin.site.register(VacaLote)