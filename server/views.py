from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Servers
from .serializer import ServerSerializer


# Create your views here.
class ServerListViewSet(viewsets.ViewSet):
    queryset=Servers.objects.all()
    def list(self,request):
        category=request.query_params.get("category")
        
        if category:
            self.queryset=self.queryset.filter(category__name=category)
        serializer=ServerSerializer(self.queryset,many=True)
        return Response(serializer.data)
            
            

