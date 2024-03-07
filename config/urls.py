from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import AnimalViewSet, CategoriaRegistroViewSet, DesmameViewSet, IdentificadorViewSet, LoteViewSet, NascimentoViewSet, PelagemViewSet, OrganizacaoViewSet, RacaViewSet, SubdivisaoViewSet, VacaLoteViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register(r"animal", AnimalViewSet)
router.register(r"categoria_registro", CategoriaRegistroViewSet)
router.register(r"desmame", DesmameViewSet)
router.register(r"identificador", IdentificadorViewSet)
router.register(r"lote", LoteViewSet)
router.register(r"nascimento", NascimentoViewSet)
router.register(r"pelagem", PelagemViewSet)
router.register(r"organizacao", OrganizacaoViewSet)
router.register(r"raca", RacaViewSet)
router.register(r"subdivisao", SubdivisaoViewSet)
router.register(r"vaca_lote", VacaLoteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        " ",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
