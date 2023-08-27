from django.shortcuts import render

# Create your views here.
# people_app/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Ceps, Endereco
from .serializers import CepsSerializer, EnderecoSerializer

class CepsViewSet(viewsets.ModelViewSet):
    queryset = Ceps.objects.all()
    serializer_class = CepsSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # <- note a lista aqui
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return super(CepsViewSet, self).create(request, *args, **kwargs)

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
     
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):  # <- note a lista aqui
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return super(EnderecoViewSet, self).create(request, *args, **kwargs)