from uuid import uuid4
from django.db import models
from .cajaingreso import Cajaingreso
from .nivel import Nivel
from .periodoContable import PeriodoContable


class Modcontable(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cajaingre = models.ForeignKey(Cajaingreso, blank=True, null=True)
    nivell = models.ForeignKey(Nivel, blank=True, null=True)
    periodocon = models.ForeignKey(PeriodoContable, blank=True, null=True)

    class Meta:
        verbose_name = "Modcontable"
        verbose_name_plural = "Modcontables"
        permissions = (
            ('list_modcontable', 'Can list modcontable'),
            ('get_modcontable', 'Can get modcontable'),
        )

    def __str__(self):
        return self.regisanual
