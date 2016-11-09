from django.conf.urls import url, include
from rest_framework import routers

from .usercashier_view import UsercashierViewSet

from .modcontable_view import ModcontableViewSet

from .cajaingreso_view import CajaingresoViewSet

from .nivel_view import NivelViewSet

from .periodoContable_view import PeriodoContableViewSet

router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)
router.register(r'cajaingresos', CajaingresoViewSet)

router.register(r'periodoContables', PeriodoContableViewSet)

router.register(r'modcontables', ModcontableViewSet)
router.register(r'nivels', NivelViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
