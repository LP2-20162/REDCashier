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
>>>>>>> 8ca5d9d1b554e7dc56beab57b192995165ada4c0
