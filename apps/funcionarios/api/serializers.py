from rest_framework import serializers
from apps.empresa.models import Empresa
from apps.funcionarios.models import Funcionario


class FuncEmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj']


class FuncionarioSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    empresa = FuncEmpSerializer(read_only=True, many=True)

    class Meta:
        model = Funcionario
        fields = ['id', 'user', 'nome', 'cpf', 'empresa']

