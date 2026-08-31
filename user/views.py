from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerialzer, RegisterSerializer


class RegisterView(generics.CreateAPIView):
    """
    POST /api/v1/user/register/
    """
    
    queryset= User.objects.all()
    serializer_class= RegisterSerializer
    permission_classes= [permissions.AllowAny]
    
class MeView(generics.RetrieveUpdateDestroyAPIView):
    """ 
    GET, PATCH, DELETE /api/v1/user/me/
    """
    serializer_class=UserSerialzer
    permission_classes= [permissions.IsAuthenticated]
    
    def get_object(self): #Khong dung id de tim user de tranh lo id user khi truyen url qua internet
        return self.request.user #DRF se tu parse userid tu token