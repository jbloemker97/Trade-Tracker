from django.db import models

class Trades(models.Model):
    ticker = models.CharField(max_length=5)
    entry_date = models.DateTimeField()
    exit_date = models.DateTimeField()
    entry_price = models.DecimalField(max_digits=6, decimal_places=2)
    exit_price = models.DecimalField(max_digits=6, decimal_places=2)
    pnl = models.DecimalField(max_digits=10, decimal_places=2)
    entry_comments = models.CharField(max_length=500)
    exit_comments = models.CharField(max_length=500)

    def __str__(self):
        return self.ticker
