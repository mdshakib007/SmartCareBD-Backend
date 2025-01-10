from django.shortcuts import render
from django.contrib.auth.models import User
from core.serializers import UserSerializer
from rest_framework import viewsets, filters

class SpecificUser(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.query_params.get('user_id')
        if user_id:
            return queryset.filter(id=user_id)
        return queryset

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [SpecificUser]

