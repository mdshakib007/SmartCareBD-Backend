from django.shortcuts import render
from doctor.serializers import DoctorSerializer, SpecializationSerializer, DesignationSerializer, AvailableTimeSerializer, ReviewSerializer
from rest_framework import viewsets, pagination, filters
from doctor.models import Doctor, Specialization, Designation, AvailableTime, Review
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class SpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(id = doctor_id)
        return query_set

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [SpecificDoctor]

class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(available_time = doctor_id)
        return query_set

class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class ReviewForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [ReviewForSpecificDoctor]
