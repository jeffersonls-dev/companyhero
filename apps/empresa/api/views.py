from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from .serializers import EmpresaSerializer
from apps.empresa.models import Empresa


class EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = EmpresaSerializer
    authentication_classes = (TokenAuthentication,SessionAuthentication)
    permissions_classes = (permissions.IsAuthenticated,)


    def get_queryset(self):
        queryset = Empresa.objects.filter()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        user = self.request.query_params.get('user', None)
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if user:
            queryset = queryset.filter(funcionario__user__username=user)
        return queryset

        @action(detail=True)
        def list(self,request,*args,**kwargs):
            return super(EmpresaViewSet, self).list(request,*args,**kwargs)
