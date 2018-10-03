from django import forms

class UpdateProfileForm(forms.Form):
    profile_image = forms.ImageField(required=False)
    full_name = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    account_balance = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    starting_balance = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))