from rest_framework import serializers
from .models import Ceps, Endereco

class CepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceps
        fields = ['id','cep']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','Endereco']