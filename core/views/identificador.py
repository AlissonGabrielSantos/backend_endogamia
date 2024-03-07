from rest_framework.viewsets import ModelViewSet

from core.models import Identificador
from core.serializers import IdentificadorSerializer

class IdentificadorViewSet(ModelViewSet):
    queryset = Identificador.objects.all()
    serializer_class = IdentificadorSerializer