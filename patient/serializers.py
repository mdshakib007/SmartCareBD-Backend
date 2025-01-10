from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        f_name = self.validated_data['first_name']
        l_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password != confirm_password:
            raise serializers.ValidationError({"Error" : "Password & confirm password doesn't match!"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"Error" : "This email is already exists!"})

        account = User(username=username, email=email, first_name=f_name, last_name=l_name)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
