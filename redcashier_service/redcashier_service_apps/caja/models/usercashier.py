from uuid import uuid4
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from .boleta import Boleta
from .nivel import Nivel


class Usercashier(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20, null=True, blank=True)
    usuario = models.CharField(max_length=20)
    perfil = models.CharField(max_length=20)
    sucursal = models.ForeignKey(Nivel, null=True, blank=True)
    bol = GenericRelation(Boleta)

    class Meta:
        verbose_name = "Usercashier"
        verbose_name_plural = "Usercashiers"
        permissions = (
            ('list_usercashier', 'Can list usercashier'),
            ('get_usercashier', 'Can get usercashier'),
        )

    def __str__(self):
        return self.nombre
