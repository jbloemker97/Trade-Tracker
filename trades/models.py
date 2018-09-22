from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Trades(models.Model):
    CHOICES = (
        ('Long', 'Long'),
        ('Short', 'Short')
    )
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('trades.Trades', on_delete=models.CASCADE, null=True)
    ticker = models.CharField(max_length=5)
    position = models.CharField(max_length=100, choices=CHOICES, default='Long')
    shares = models.PositiveIntegerField(default=0)
    entry_date = models.DateTimeField(timezone.now()) # xx/xx/xx
    exit_date = models.DateTimeField(timezone.now(), blank=True, null=True) # xx/xx/xx
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)
    exit_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pnl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    entry_comments = models.CharField(max_length=500)
    exit_comments = models.CharField(max_length=500, blank=True, null=True)
    success = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
