from django.conf.urls import url, include
from rest_framework import routers

from .usercashier_view import UsercashierViewSet
<<<<<<< HEAD
from .nivel_view import NivelViewSet
=======
from .cajaingreso_view import CajaingresoViewSet
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4


router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)
router.register(r'cajaingresos', CajaingresoViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]


router = routers.DefaultRouter()

router.register(r'nivel', NivelViewSet)

urlpatterns = [

    url(r'^', include(router.urls)),

]
