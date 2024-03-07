from rest_framework.serializers import ModelSerializer

from core.models import CategoriaRegistro

class CategoriaRegistroSerializer(ModelSerializer):
    class Meta:
        model = CategoriaRegistro
        fields = "__all__"
        depth = 1