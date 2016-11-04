from uuid import uuid4
from django.db import models


class Modcontable(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    contanual = models.CharField(max_length=50, blank=True, null=True)
    regisanual = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Modcontable"
        verbose_name_plural = "Modcontables"
        permissions = (
            ('list_modcontable', 'Can list modcontable'),
            ('get_modcontable', 'Can get modcontable'),
        )

    def __str__(self):
        return self.regisanual
