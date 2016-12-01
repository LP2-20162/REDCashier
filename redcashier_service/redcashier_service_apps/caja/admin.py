from django.contrib import admin
from .models.usercashier import Usercashier
from .models.periodoContable import PeriodoContable
from .models.modcontable import Modcontable

from .models.nivel import Nivel

from .models.cajaingreso import Cajaingreso

# Register your models here.


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


class CajaingresoAdmin(admin.ModelAdmin):

    """docstring for CategoriaAdmin"""

    list_display = ("concepto", "nivel", "fecha",)
    search_fields = ("concepto", "nivel",)
    list_per_page = 3

admin.site.register(Cajaingreso, CajaingresoAdmin)
