from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pictures')
    full_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=9, blank=True)
    education = models.CharField(max_length=100, blank=True)
    residency = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
