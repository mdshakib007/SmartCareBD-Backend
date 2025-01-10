from django.shortcuts import render, redirect
from rest_framework import viewsets
from patient.serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer
from patient.models import Patient
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class UserRegistrationAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/patient/activate/{uid}/{token}"
            
            email_sub = "Confirm Your Email"
            email_body = render_to_string('patient/confirm_email.html', {"confirm_link" : confirm_link})
            email = EmailMultiAlternatives(email_sub, '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response("Please check confirmation email!")
        return Response(serializer.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'patient/success_register.html')
    else:
        return redirect("register")
    

class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'invalid user authentication!'})
        return Response(serializer.errors)


class UserLogoutAPIView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")
