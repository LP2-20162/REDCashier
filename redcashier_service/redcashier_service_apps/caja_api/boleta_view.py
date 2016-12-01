import logging

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from django.contrib.contenttypes.models import ContentType

from redcashier_service_apps.caja.models.boleta import Boleta

from redcashier_service_apps.utils.security import log_params
from redcashier_service_apps.utils.permissions import ModelPermission
from redcashier_service_apps.utils.pagination import ModelPagination

from .usercashier_view import UsercashierSerializer
from redcashier_service_apps.caja.models.usercashier import Usercashier
from generic_relations.relations import GenericRelatedField

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


#@override_settings(ROOT_URLCONF='generic_relations')


# class GenericRelatedFieldSerialization(object):

#    def setUp(self):
#        Boleta.objects.create(tagged_item=self.bookmark, tag='django')
#        Boleta.objects.create(tagged_item=self.bookmark, tag='python')
#        self.usercashier = Usercashier.objects.create(text='Remember the milk')
#        Boleta.objects.create(tagged_item=self.Usercashier, tag='reminder')

        # Nivel.objects.create(content_object=self.Usercashier, name='attached')
        # Nivel.objects.create(name='detached')

#    def relationsA_as_hyperlinks(self):
class BoletaSerializer(serializers.ModelSerializer):

    b_nivel = serializers.ReadOnlyField(
        source='nivel.nombreSuc')
    # b_userCaja = serializers.ReadOnlyField(
    #   source='usercashier.nombre')
    # precio = serializers.ReadOnlyField(
    #    write_only='Boleta.cantidad * Boleta.precioUn'
    #)tagged_object = serializers.GenericRelatedField({
    usuarioCaja = GenericRelatedField(
        {
            Usercashier: serializers.HyperlinkedRelatedField(
                view_name='Usercashier-detail',
                queryset=Usercashier.objects.all()),
        },
        read_only=True,
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
    # content_type = ContentType.objects.get_for_model(Usercashier)
    # usuarioCaja = Boleta.objects.filter(content_type=content_type)

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

   # def bolet_detail(request):
    #    instance = get_object_or_404(Boleta, id=3)
     #   context = {
    #        "title": "detail"
    #        "instance":

    #    }
    #    return render(request,"index.html",context)
    # def bolet_list(request):
    #    self.queryset= Boleta.objects.all()
    #    context = {

    #    }
    #    return render(request,"index.html",context)
