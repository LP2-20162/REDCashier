from django.conf.urls import url, include
from rest_framework import routers

from .usercashier_view import UsercashierViewSet

from .modcontable_view import ModcontableViewSet

from .cajaingreso_view import CajaingresoViewSet


router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)
router.register(r'cajaingresos', CajaingresoViewSet)

router.register(r'modcontables', ModcontableViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
