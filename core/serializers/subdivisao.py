from rest_framework.serializers import ModelSerializer

from core.models import Subdivisao

class SubdivisaoSerializer(ModelSerializer):
    class Meta:
        model = Subdivisao
        fields = "__all__"