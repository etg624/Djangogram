from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_pic = models.ImageField(null=True, blank=True, upload_to="uploads/", default="assets/")
    def __str__(self):
        return self.username