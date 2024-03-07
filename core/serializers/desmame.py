from rest_framework.serializers import ModelSerializer

from core.models import Desmame

class DesmameSerializer(ModelSerializer):
    class Meta:
        model = Desmame
        fields = "__all__"