from rest_framework.viewsets import ModelViewSet

from core.models import Lote
from core.serializers import LoteSerializer

class LoteViewSet(ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer