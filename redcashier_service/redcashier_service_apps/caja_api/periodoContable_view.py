from rest_framework import serializers, viewsets


from redcashier_service_apps.caja.models.periodoContable import PeriodoContable


class PeriodoContableSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeriodoContable
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"


class PeriodoContableViewSet(viewsets.ModelViewSet):
    queryset = PeriodoContable.objects.all()
    serializer_class = PeriodoContableSerializer
