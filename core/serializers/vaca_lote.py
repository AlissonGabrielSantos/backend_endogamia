from rest_framework.serializers import ModelSerializer

from core.models import VacaLote

class VacaLoteSerializer(ModelSerializer):
    class Meta:
        model = VacaLote
        fields = "__all__"
        #depth = 1