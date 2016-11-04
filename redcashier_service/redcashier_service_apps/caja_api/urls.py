from django.conf.urls import url, include
from rest_framework import routers

from .usercashier_view import UsercashierViewSet
from .nivel_view import NivelViewSet


router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]


router = routers.DefaultRouter()

router.register(r'nivel', NivelViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
