import logging

from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from redcashier_service_apps.caja.models.cajaingreso import Cajaingreso

from redcashier_service_apps.utils.security import log_params
from redcashier_service_apps.utils.permissions import ModelPermission
from redcashier_service_apps.utils.pagination import ModelPagination


from rest_framework import permissions
from django.utils.translation import ugettext as _  # , ungettext


class MiPermission(permissions.BasePermission):
    """
    Ejemplo de permiso para microrecursos @list_route o @detail_route
    """

    def has_permission(self, request, view):
        perms = ('caja.list_cajaingreso',)  # cambie aqui el permiso
        if request.user.has_perms(perms):
            return True
        else:
            log.info(
                _('Permission denied. You don\'t have permission to %s.'
                  ) % (perms),
                extra=log_params(request)
            )
            return False


class CajaingresoSerializer(serializers.ModelSerializer):

    c_sucursal = serializers.ReadOnlyField(
        source='nivel.nombreSuc')

    class Meta:
        model = Cajaingreso
        # fields = ('url', 'username', 'email', 'is_staff')
        fields = "__all__"

from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CajaingresoViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Cajaingreso.objects.all()
    serializer_class = CajaingresoSerializer
    permission_classes = [ModelPermission, ]
    #permission_replace_by_model = 'cat.autor2'
    #pagination_class = LargeResultsSetPagination

    def get_queryset(self):

        search = self.request.query_params.get('query', None)
        if search:
            print('search=', search)
            self.queryset = Cajaingreso.objects.filter(
                nombre__icontains=search)
        return self.queryset

    @list_route(url_path='export', methods=['get'],
                permission_classes=[MiPermission])
    def reporte_cajaingresos(self, request, *args, **kwargs):
        lista = []
        pre_query = self.get_queryset().values()
        for x in pre_query:
            lista.append([x['concepto'], x['sucursal']])
        print(lista)
        #data = Autor.objects.pdf(lista, 'mi primer reporte')
        data = self.get_queryset().filter()
        # return Response({'detail':str('Exportado a PDF')})
        # return Response(data)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)
