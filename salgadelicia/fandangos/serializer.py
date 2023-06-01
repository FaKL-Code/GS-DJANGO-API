from rest_framework import serializers
from fandangos.models import Doador, Doacao
from django.contrib.auth import get_user_model

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ['id', 'nome', 'cpf', 'email', 'telefone', 'endereco']

class DoacaoSerializer(serializers.ModelSerializer):
    
    doador = serializers.ReadOnlyField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Doacao
        fields = ['id', 'doador', 'volume', 'data_doacao', 'data_retirada']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"