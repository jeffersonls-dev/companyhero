from rest_framework import serializers
from apps.empresa.models import Empresa
from apps.funcionarios.models import Funcionario


class EmpresaSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = ['nome', 'cnpj', 'user']

    def get_user(self, obj):
        response = []
        for funcionario in Funcionario.objects.filter(empresa=obj):
            user_profile = EmpFuncionarioSerializer(
                funcionario,
                context={'request': self.context['request']})
            response.append(user_profile.data)
        return response


class EmpFuncionarioSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Funcionario
        fields = ['nome', 'user']
