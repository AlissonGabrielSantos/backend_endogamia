from rest_framework.viewsets import ModelViewSet

from core.models import Desmame
from core.serializers import DesmameSerializer

class DesmameViewSet(ModelViewSet):
    queryset = Desmame.objects.all()
    serializer_class = DesmameSerializer