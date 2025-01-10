from rest_framework.routers import DefaultRouter
from django.urls import path, include
from patient.views import PatientViewSet, UserRegistrationAPIView, activate, UserLoginAPIView, UserLogoutAPIView

router = DefaultRouter()
router.register('list', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name="register"),
    path('activate/<uid64>/<token>/', activate, name="activate"),
    path('login/', UserLoginAPIView.as_view(), name="login"),
    path('logout/', UserLogoutAPIView.as_view(), name="logout"),
]

