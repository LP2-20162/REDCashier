from django.contrib import admin
from .models.usercashier import Usercashier
from .models.periodoContable import PeriodoContable
from .models.modcontable import Modcontable
from .models.nivel import Nivel
from .models.cajaingreso import Cajaingreso
from .models.boleta import Boleta

# Register your models here.


class BoletaAdmin(admin.ModelAdmin):
    """docstring for BoletaAdmin"""
    list_display = ("cantidad", "detalle", "precioUn", "importe",
                    "igv", "precioTotal", "content_type")
    search_fields = ("nombre", "codigo", "nivel")
    list_per_page = 9

admin.site.register(Boleta, BoletaAdmin)


class PeriodoContableAdmin(admin.ModelAdmin):

    """docstring for PeriodoContableAdmin"""

    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 3


admin.site.register(PeriodoContable, PeriodoContableAdmin)


# Register your models here.


class UsercashierAdmin(admin.ModelAdmin):
    """docstring for UsercashierAdmin"""
    list_display = ("nombre", "apellido", "usuario")
    search_fields = ("nombre", "usuario",)
    list_per_page = 3

admin.site.register(Usercashier, UsercashierAdmin)

#list_display = ("nombre", "apellido", "usuario")
#   search_fields = ("nombre", "usuario",)
#   list_per_page = 3


class NivelAdmin(admin.ModelAdmin):
    """docstring for NivelAdmin"""
    '''list_display = ("nombre", "apellido", "usuario",)
    search_fields = ("nombre", "usuario",)
    list_per_page = 3'''
admin.site.register(Nivel, NivelAdmin)


class ModcontableAdmin(admin.ModelAdmin):
    """docstring for ModcontableAdmin"""
    list_display = ("contanual", "regisanual",)
    search_fields = ("contanual", "regisanual",)
    list_per_page = 3

admin.site.register(Modcontable, ModcontableAdmin)


#list_display = ("nombre", "apellido", "usuario")
#   search_fields = ("nombre", "usuario",)
#   list_per_page = 3

class CajaingresoAdmin(admin.ModelAdmin):

    """docstring for CategoriaAdmin"""

    list_display = ("concepto", "sucursal", "total")
    search_fields = ("concepto", "sucursal",)
    list_per_page = 3

admin.site.register(Cajaingreso, CajaingresoAdmin)
