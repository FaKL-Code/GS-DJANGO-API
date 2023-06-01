from fandangos.models import Doador, Doacao
from fandangos.serializer import DoadorSerializer, DoacaoSerializer, UserSerializer, AdminSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

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

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = get_user_model().objects.all()

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return AdminSerializer
        return UserSerializer 
