from rest_framework.viewsets import ModelViewSet

from core.models import Pelagem
from core.serializers import PelagemSerializer

class PelagemViewSet(ModelViewSet):
    queryset = Pelagem.objects.all()
    serializer_class = PelagemSerializer