from uuid import uuid4
from django.db import models


class Cajaingreso(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    concepto = models.CharField(max_length=60)
    #'''anulado = models.BooleanField(default=True)'''
    cuentaEmpresa = models.IntegerField(default=170)
    cuentaCliente = models.IntegerField(default=170)
    cuentaGanancia = models.IntegerField(default=170)
    cuentaVenta = models.IntegerField(default=170)
    #'''numDocumento = models.CharField(max_lenght=9, null=True, blank=True'''
    entregadoA = models.CharField(max_length=60, null=True, blank=True)
    #fecha = models.DateTimeField(max_length=60, null=True, blank=True)
    #'''precio = models.DecimalField(max_digits=5, decimal_place=2)'''
    sucursal = models.IntegerField(default=170)
    total = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Cajaingreso"
        verbose_name_plural = "Cajaingresos"

    def __str__(self):
        pass
