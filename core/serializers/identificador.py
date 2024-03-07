from rest_framework.serializers import ModelSerializer

from core.models import Identificador

class IdentificadorSerializer(ModelSerializer):
    class Meta:
        model = Identificador
        fields = "__all__"