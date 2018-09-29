from django import forms

class UpdateProfileForm(forms.Form):
    profile_image = forms.ImageField()
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    account_balance = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    starting_balance = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))