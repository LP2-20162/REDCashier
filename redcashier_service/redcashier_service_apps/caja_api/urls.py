from django.conf.urls import url, include
from rest_framework import routers

from .usercashier_view import UsercashierViewSet
from .cajaingreso_view import CajaingresoViewSet


router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)
router.register(r'cajaingresos', CajaingresoViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
