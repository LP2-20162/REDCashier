from uuid import uuid4
from django.db import models
from .nivel import Nivel
from .cliente import Cliente
from .usercashier import Usercashier


class Boleta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cantidad = models.IntegerField(default=170)
    detalle = models.CharField(max_length=40)
    precioUn = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    importe = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    igv = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    precioTotal = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    nivel = models.ForeignKey(Nivel, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    usercashiers = models.ForeignKey(Usercashier, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Boleta"
        verbose_name_plural = "Boletas"
        permissions = (
            ('list_boleta', 'Can list boleta'),
            ('get_boleta', 'Can get boleta'),
        )

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.cantidad, self.detalle,
                                      self.importe, self.igv, self.precioTotal, self.fecha)


# def Calcularprecio(cantidad, precioUn):
#    total = cantidad * precioUn
#    return total


# def calcularTotal(total):
#    for i in range(10):
#        i = i + +
#        precioTotal = total + i
#    return precioTotal
