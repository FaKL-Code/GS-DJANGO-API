from fandangos.models import Doador, Doacao
from fandangos.serializer import DoadorSerializer, DoacaoSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class DoadoresViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Doador.objects.all()
    
    def get_serializer_class(self):
        return DoadorSerializer    

class DoacoesViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Doacao.objects.all()
    
    def get_serializer_class(self):
        return DoacaoSerializer    

