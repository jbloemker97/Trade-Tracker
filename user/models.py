from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    account_balance = models.FloatField(blank=True)
    starting_balance = models.FloatField(blank=True, default=None)

    @property
    def photo_url(self):
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url

    def __str__(self):
        return self.full_name