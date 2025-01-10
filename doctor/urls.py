from rest_framework.routers import DefaultRouter
from django.urls import path, include
from doctor.views import DoctorViewSet, DesignationViewSet, SpecializationViewSet, AvailableTimeViewSet, ReviewViewSet

router = DefaultRouter()
router.register('list', DoctorViewSet)
router.register('designations', DesignationViewSet)
router.register('specializations', SpecializationViewSet)
router.register('available_times', AvailableTimeViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

