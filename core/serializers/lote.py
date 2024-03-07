from rest_framework.serializers import ModelSerializer

from core.models import Lote

class LoteSerializer(ModelSerializer):
    class Meta:
        model = Lote
        fields = "__all__"
        #depth = 1