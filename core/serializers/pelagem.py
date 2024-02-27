from rest_framework.serializers import ModelSerializer

from core.models import Pelagem

class PelagemSerializer(ModelSerializer):
    class Meta:
        model = Pelagem
        fields = "__all__"