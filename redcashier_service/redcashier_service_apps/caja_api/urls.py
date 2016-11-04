from django.conf.urls import url, include
from rest_framework import routers

from .periodoContable_view import PeriodoContableViewSet

router = routers.DefaultRouter()

router.register(r'periodoContable', PeriodoContableViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
