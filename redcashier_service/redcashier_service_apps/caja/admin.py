from django.contrib import admin
<<<<<<< HEAD
from django.contrib import admin
from .models.usercashier import Usercashier
from .models.periodoContable import PeriodoContable
from .models.modcontable import Modcontable

# Register your models here.


class PeriodoContableAdmin(admin.ModelAdmin):

    """docstring for PeriodoContableAdmin"""

    list_display = ("nombre", "codigo", "estado")
    search_fields = ("nombre", "codigo",)
    list_per_page = 3


admin.site.register(PeriodoContable, PeriodoContableAdmin)
=======
from .models.usercashier import Usercashier
<<<<<<< HEAD
from .models.nivel import Nivel
=======

from .models.modcontable import Modcontable

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
>>>>>>> 9d0b2ebd21c6c842e292e25744c1d84516bfc60a
=======
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
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
