from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import UserViewSet

router = DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

