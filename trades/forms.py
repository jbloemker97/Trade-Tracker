from django import forms

class EntryForm(forms.Form):
    ticker = forms.CharField(max_length=5)
    entry_date = forms.DateTimeField()
    exit_date = forms.DateTimeField()
    entry_price = forms.DecimalField(max_digits=6, decimal_places=2)
    exit_price = forms.DecimalField(max_digits=6, decimal_places=2)
    pnl = forms.DecimalField(max_digits=10, decimal_places=2)
    entry_comments = forms.CharField(max_length=500, widget=forms.Textarea)
    exit_comments = forms.CharField(max_length=500, widget=forms.Textarea)