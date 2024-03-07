from rest_framework.serializers import ModelSerializer

from core.models import Organizacao

class OrganizacaoSerializer(ModelSerializer):
    class Meta:
        model = Organizacao
        fields = "__all__"
        depth = 1