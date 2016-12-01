from uuid import uuid4
from django.db import models
from .nivel import Nivel
#from .usercashier import Usercashier
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Boleta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cantidad = models.IntegerField(default=170)
    detalle = models.CharField(max_length=40)
    precioUn = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    importe = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    igv = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    precioTotal = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    nivel = models.ForeignKey(Nivel)
    cliente = models.CharField(max_length=30)
    #usercashiers = models.ForeignKey(Usercashier)
    fecha = models.DateField(null=True, blank=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

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
