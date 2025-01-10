from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    full_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="patient/images/")
    mobile = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if self.user:
            f_name = self.user.first_name
            l_name = self.user.last_name
            self.full_name = f"{f_name} {l_name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

