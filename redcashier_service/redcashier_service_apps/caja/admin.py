from django.contrib import admin
from .models.usercashier import Usercashier
<<<<<<< HEAD
from .models.nivel import Nivel
=======
from .models.cajaingreso import Cajaingreso
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
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
class NivelAdmin(admin.ModelAdmin):
    """docstring for NivelAdmin"""
    '''list_display = ("nombre", "apellido", "usuario",)
    search_fields = ("nombre", "usuario",)
    list_per_page = 3'''
admin.site.register(Nivel, NivelAdmin)
=======
class CajaingresoAdmin(admin.ModelAdmin):

    """docstring for CategoriaAdmin"""

    list_display = ("concepto", "sucursal", "total")
    search_fields = ("concepto", "sucursal",)
    list_per_page = 3

admin.site.register(Cajaingreso, CajaingresoAdmin)
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
