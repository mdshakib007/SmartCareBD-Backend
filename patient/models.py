from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    image = models.ImageField(upload_to="patient/images/")
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

