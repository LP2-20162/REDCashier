from django.contrib import admin
from .models.usercashier import Usercashier
from .models.nivel import Nivel
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
