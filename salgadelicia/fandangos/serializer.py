from rest_framework import serializers
from fandangos.models import Doador, Doacao

class DoadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doador
        fields = ['id', 'nome', 'cpf', 'email', 'telefone', 'endereco']

class DoacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doacao
        fields = ['id', 'doador', 'volume', 'data_doacao', 'data_retirada']