from django.shortcuts import render
from rest_framework import viewsets
from contact_us.serializers import ContactUsSerializer
from contact_us.models import ContactUs
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContactUsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
