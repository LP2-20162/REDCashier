from django.contrib import admin
from .models.usercashier import Usercashier

from .models.modcontable import Modcontable

from .models.cajaingreso import Cajaingreso

# Register your models here.


class UsercashierAdmin(admin.ModelAdmin):
    """docstring for UsercashierAdmin"""
    list_display = ("nombre", "apellido", "usuario")
    search_fields = ("nombre", "usuario",)
    list_per_page = 3


admin.site.register(Usercashier, UsercashierAdmin)


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
