from rest_framework import serializers, viewsets
#from django.db.models import Q
#from operator import __or__ as OR
#from functools import reduce

from redcashier_service_apps.caja.models.nivel import Nivel


class NivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nivel
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
