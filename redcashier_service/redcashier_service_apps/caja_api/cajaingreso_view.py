from rest_framework import serializers, viewsets


from redcashier_service_apps.caja.models.cajaingreso import Cajaingreso


class CajaingresoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cajaingreso
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"


class CajaingresoViewSet(viewsets.ModelViewSet):
    queryset = Cajaingreso.objects.all()
    serializer_class = CajaingresoSerializer
