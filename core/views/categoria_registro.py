from rest_framework.viewsets import ModelViewSet

from core.models import CategoriaRegistro
from core.serializers import CategoriaRegistroSerializer

class CategoriaRegistroViewSet(ModelViewSet):
    queryset = CategoriaRegistro.objects.all()
    serializer_class = CategoriaRegistroSerializer