import logging

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from redcashier_service_apps.caja.models.boleta import Boleta

from redcashier_service_apps.utils.security import log_params
from redcashier_service_apps.utils.permissions import ModelPermission
from redcashier_service_apps.utils.pagination import ModelPagination


from rest_framework import permissions
from django.utils.translation import ugettext as _  # , ungettext

log = logging.getLogger(__name__)


class MiPermission(permissions.BasePermission):
    """
    Ejemplo de permiso para microrecursos @list_route o @detail_route
    """

    def has_permission(self, request, view):
        perms = ('caja.list_boleta',)
        if request.user.has_perms(perms):
            return True
        else:
            log.info(
                _('Permission denied. You don\'t have permission to %s.'
                  ) % (perms),
                extra=log_params(request)
            )
            return False


class BoletaSerializer(serializers.ModelSerializer):

    b_nivel = serializers.ReadOnlyField(
        source='nivel.nombreSuc')
    b_client = serializers.ReadOnlyField(
        source='cliente.nombre')
    # b_userCaja = serializers.ReadOnlyField(
    # source='usercashier.nombre')
    precio = serializers.ReadOnlyField(
        source=''
    )

    class Meta:
        model = Boleta
        fields = "__all__"

from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class BoletaViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Boleta.objects.all()
    serializer_class = BoletaSerializer
    permission_classes = [ModelPermission, ]

    def get_queryset(self):

        search = self.request.query_params.get('query', None)
        if search:
            print ('search=', search)
            self.queryset = Boleta.objects.filter(nombre__icontains=search)
        return self.queryset

    @list_route(url_path='export', methods=['get'],
                permission_classes=[MiPermission])
    def reporte_bolet(self, request, *args, **kwargs):
        lista = []
        pre_query = self.get_queryset().values()
        for x in pre_query:
            lista.append([x['detalle'], x['importe']])
        print(lista)
        # data = Autor.objects.pdf(lista, 'mi primer reporte')
        data = self.get_queryset().filter()
        # return Response({'detail':str('Exportado a PDF')})
        # return Response(data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
