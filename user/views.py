from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def register(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'registration/register.html', context)