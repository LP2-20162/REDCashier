from django.conf.urls import url, include
from rest_framework import routers

<<<<<<< HEAD
from .periodoContable_view import PeriodoContableViewSet

router = routers.DefaultRouter()

router.register(r'periodoContable', PeriodoContableViewSet)
=======
from .usercashier_view import UsercashierViewSet
from .cajaingreso_view import CajaingresoViewSet


router = routers.DefaultRouter()

router.register(r'usercashiers', UsercashierViewSet)
<<<<<<< HEAD
>>>>>>> 8ca5d9d1b554e7dc56beab57b192995165ada4c0
=======
router.register(r'cajaingresos', CajaingresoViewSet)
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4

urlpatterns = [

    url(r'^', include(router.urls)),

]
