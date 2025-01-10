from django.urls import path, include
from appointment.serializers import AppointmentSerializer
from appointment.views import AppointmentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

