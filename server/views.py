from django.shortcuts import render
from django.db.models import Count
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError,AuthenticationFailed
from .models import Servers
from .serializer import ServerSerializer


# Create your views here.
class ServerListViewSet(viewsets.ViewSet):
    queryset=Servers.objects.all()
    def list(self,request):
        category=request.query_params.get("category")
        qty=request.query_params.get('qty')
        by_user=request.query_params.get('by-user')
        by_serverid=request.query_params.get('by-serverid')
        with_num_members=request.query_params.get('with-num-members')
        if by_user or by_serverid and not request.user.is_authenticated:
            raise AuthenticationFailed()
        if category:
            self.queryset=self.queryset.filter(category__name=category)
        if by_user:
            user_id=request.user.id
            self.queryset=self.queryset.filter(members=user_id)
        if with_num_members:
            self.queryset=self.queryset.annotate(num_members=Count('members'))       
        if qty:
            self.queryset=self.queryset[: int(qty)]
        if by_serverid:
            try:
                self.queryset=self.queryset.filter(id=by_serverid)
                if not self.queryset.exists():
                    raise ValidationError(detail='server not found')
            except ValueError:
                raise ValidationError(detail="server not found")
                            
        serializer=ServerSerializer(self.queryset,many=True)
        return Response(serializer.data)
            
            

