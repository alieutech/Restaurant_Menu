from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MenuSerializers
from rest_framework.permissions import AllowAny
from .models import Menu

# Create your views here.


class MenuAPIView(APIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers
    permission_classes = [AllowAny]