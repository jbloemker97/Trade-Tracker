from django import forms

class EntryForm(forms.Form):
    CHOICES = (
        ('Long', 'Long'),
        ('Short', 'Short')
    )
    ticker = forms.CharField(max_length=5)
    position = forms.CharField(widget=forms.Select(choices=CHOICES), required=True)
    entry_date = forms.DateTimeField()
    exit_date = forms.DateTimeField(required=False)
    entry_price = forms.DecimalField(max_digits=6, decimal_places=2)
    exit_price = forms.DecimalField(max_digits=6, decimal_places=2, required=False)
    pnl = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    entry_comments = forms.CharField(max_length=500, widget=forms.Textarea)
    exit_comments = forms.CharField(max_length=500, widget=forms.Textarea, required=False)