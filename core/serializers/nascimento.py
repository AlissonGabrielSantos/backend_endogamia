from rest_framework.serializers import ModelSerializer

from core.models import Nascimento

class NascimentoSerializer(ModelSerializer):
    class Meta:
        model = Nascimento
        fields = "__all__"
        depth = 1