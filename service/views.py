from django.shortcuts import render
from service.serializers import ServiceSerializer
from service.models import Service
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer