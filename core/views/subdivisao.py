from rest_framework.viewsets import ModelViewSet

from core.models import Subdivisao
from core.serializers import SubdivisaoSerializer

class SubdivisaoViewSet(ModelViewSet):
    queryset = Subdivisao.objects.all()
    serializer_class = SubdivisaoSerializer