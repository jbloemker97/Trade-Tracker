from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    profile_image = models.ImageField('profile_image', blank=True)
    account_balance = models.FloatField(blank=True)
    starting_balance = models.FloatField(blank=True, default=None)

    def __str__(self):
        return self.full_name
