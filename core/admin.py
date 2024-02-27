from django.contrib import admin
from .models import Animal, Nascimento, Pelagem, Raca

#admin.site.register(Animal)
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id_animal',)
    search_fields = ('id_animal',)
    list_filter = ('id_animal',)
    ordering = ('id_animal',)

    
admin.site.register(Nascimento)
admin.site.register(Pelagem)
admin.site.register(Raca)   

