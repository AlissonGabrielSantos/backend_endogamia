from rest_framework.viewsets import ModelViewSet

from core.models import VacaLote
from core.serializers import VacaLoteSerializer

class VacaLoteViewSet(ModelViewSet):
    queryset = VacaLote.objects.all()
    serializer_class = VacaLoteSerializer