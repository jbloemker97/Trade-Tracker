from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/trades')
        
    return render(request, 'registration/registration.html', { 'form':UserCreationForm() })

def account(request):
    return render(request, 'registration/my_account.html')