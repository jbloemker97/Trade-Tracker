from django.db import models
from django.utils import timezone

class Trades(models.Model):
    CHOICES = (
        ('Long', 'Long'),
        ('Short', 'Short')
    )
    ticker = models.CharField(max_length=5)
    position = models.CharField(max_length=100, choices=CHOICES, default='Long')
    shares = models.PositiveIntegerField(default=0)
    entry_date = models.DateTimeField(timezone.now())
    exit_date = models.DateTimeField(timezone.now(), blank=True, null=True)
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)
    exit_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pnl = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    entry_comments = models.CharField(max_length=500)
    exit_comments = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.ticker
