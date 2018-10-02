from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import UpdateProfileForm
from .models import Profile
from django.urls import reverse
from django.conf import settings


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
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)

        full_name = request.POST.get('full_name')
        profile_image = request.FILES.get('profile_image')
        account_balance = request.POST.get('account_balance')
        starting_balance = request.POST.get('starting_balance')

        print(profile_image)

        profile, created = Profile.objects.get_or_create(
            user=request.user,
            defaults={
                'full_name': full_name,
                'profile_image': profile_image,
                'account_balance': account_balance,
                'starting_balance': starting_balance
            }
        )

        if not created:
            Profile.objects.filter(user_id=request.user.id).update(
                user=request.user,
                full_name=full_name,
                profile_image=profile_image,
                account_balance=account_balance,
                starting_balance=starting_balance
            )

        return HttpResponseRedirect(reverse('user:my_account'))
    else:
        form = UpdateProfileForm()
        data = Profile.objects.filter(user=request.user)
        context = { 
            'form': form,
            'data': data 
        }
        print(settings.MEDIA_URL)
        print(settings.MEDIA_ROOT)

        return render(request, 'registration/my_account.html', context)


