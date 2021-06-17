from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .serializers import FuncionarioSerializer
from apps.funcionarios.models import Funcionario


class FuncionarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = FuncionarioSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        queryset = Funcionario.objects.filter()
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        user = self.request.query_params.get('user', None)
        if id:
            queryset = queryset.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        if user:
            queryset = queryset.filter(user__username=user)
        return queryset

    def list(self, request, *args, **kwargs):
        return super(FuncionarioViewSet, self).list(request, *args, **kwargs)