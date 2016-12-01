from uuid import uuid4
from django.db import models
from .nivel import Nivel


class Cajaingreso(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    fecha = models.DateField(null=True, blank=True)
    nivel = models.ForeignKey(Nivel, null=True, blank=True)
    concepto = models.CharField(max_length=60)
    fecha = models.DateField(null=True, blank=True)
    cuentaEmpresa = models.IntegerField(default=170)
    cuentaCliente = models.IntegerField(default=170)
    cuentaGanancia = models.IntegerField(default=170)
    cuentaVenta = models.IntegerField(default=170)
    entregadoA = models.CharField(max_length=60, null=True, blank=True)
    total = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Cajaingreso"
        verbose_name_plural = "Cajaingresos"
        permissions = (
            ('list_cajaingreso', 'Can list cajaingreso'),
            ('get_cajaingreso', 'Can get cajaingreso'),
        )

    def __str__(self):
        return '%s %s' % (self.concepto, self.nivel)
