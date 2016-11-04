from rest_framework import serializers, viewsets

from redcashier_service_apps.caja.models.modcontable import Modcontable


class ModcontableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Modcontable
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"


class ModcontableViewSet(viewsets.ModelViewSet):
    queryset = Modcontable.objects.all()
    serializer_class = ModcontableSerializer
