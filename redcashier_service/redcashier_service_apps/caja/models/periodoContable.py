from uuid import uuid4
from django.db import models


class PeriodoContable(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=15, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fechInicio = models.DateField(null=True, blank=True)
    fechFin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "PeriodoContable"
        verbose_name_plural = "PeriodoContables"

        permissions = (
            ('list_periodoContable', 'Can list periodoContable'),
            ('get_periodoContable', 'Can get periodoContable'),
        )

    def __str__(self):
        return self.nombre
