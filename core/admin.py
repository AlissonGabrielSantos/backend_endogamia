from django.contrib import admin
from .models import Animal, Raca, Nascimento, Pelagem

admin.site.register(Animal)
admin.site.register(Raca)   
admin.site.register(Nascimento)
admin.site.register(Pelagem)