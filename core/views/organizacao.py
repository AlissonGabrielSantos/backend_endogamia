from rest_framework.viewsets import ModelViewSet

from core.models import Organizacao
from core.serializers import OrganizacaoSerializer

class OrganizacaoViewSet(ModelViewSet):
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoSerializer