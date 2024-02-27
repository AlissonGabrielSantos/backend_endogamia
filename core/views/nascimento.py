from rest_framework.viewsets import ModelViewSet

from core.models import Nascimento
from core.serializers import NascimentoSerializer

class NascimentoViewSet(ModelViewSet):
    queryset = Nascimento.objects.all()
    serializer_class = NascimentoSerializer