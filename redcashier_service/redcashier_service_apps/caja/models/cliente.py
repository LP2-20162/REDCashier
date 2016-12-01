from uuid import uuid4
from django.db import models


class Cliente(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    docIdentidad = models.CharField(max_length=16)
    direccion = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre
