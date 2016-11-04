from django.db import models


class Usercashier(models.Model):

    nombre = models.CharField(max_length=20)
    usuario = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    perfil = models.CharField(max_length=20)
    password = models.
    sucursal =

    class Meta:
        verbose_name = "Usercashier"
        verbose_name_plural = "Usercashiers"

    def __str__(self):
        pass
