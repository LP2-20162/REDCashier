from django.contrib import admin
<<<<<<< HEAD
from .models.periodoContable import PeriodoContable

# Register your models here.


class PeriodoContableAdmin(admin.ModelAdmin):

    """docstring for PeriodoContableAdmin"""

    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 3


admin.site.register(PeriodoContable, PeriodoContableAdmin)
=======
from .models.usercashier import Usercashier
from .models.cajaingreso import Cajaingreso
# Register your models here.


class UsercashierAdmin(admin.ModelAdmin):
    """docstring for UsercashierAdmin"""
    list_display = ("nombre", "apellido", "usuario")
    search_fields = ("nombre", "usuario",)
    list_per_page = 3


admin.site.register(Usercashier, UsercashierAdmin)


<<<<<<< HEAD
#list_display = ("nombre", "apellido", "usuario")
#   search_fields = ("nombre", "usuario",)
#   list_per_page = 3
>>>>>>> 8ca5d9d1b554e7dc56beab57b192995165ada4c0
=======
class CajaingresoAdmin(admin.ModelAdmin):

    """docstring for CategoriaAdmin"""

    list_display = ("concepto", "sucursal", "total")
    search_fields = ("concepto", "sucursal",)
    list_per_page = 3

admin.site.register(Cajaingreso, CajaingresoAdmin)
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
