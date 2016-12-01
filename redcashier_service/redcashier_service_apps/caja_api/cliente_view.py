from rest_framework import serializers, viewsets

from redcashier_service_apps.caja.models.cliente import Cliente


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
