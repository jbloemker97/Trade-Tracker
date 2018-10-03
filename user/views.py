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
            user_profile = Profile.objects.get(user=request.user)
            user_profile.user = request.user
            user_profile.full_name = full_name
            user_profile.profile_image = profile_image
            user_profile.account_balance = account_balance
            user_profile.starting_balance = starting_balance
            user_profile.save()

        return HttpResponseRedirect(reverse('user:my_account'))
    else:
        data = Profile.objects.filter(user_id=request.user.id)
        form = UpdateProfileForm(initial={'profile_image': data[0].profile_image, 'full_name': data[0].full_name, 'account_balance': data[0].account_balance, 'starting_balance': data[0].starting_balance})
        context = { 
            'form': form,
            'data': data 
        }

        # Determine % change
        if data[0]:
            percent_change = ((data[0].account_balance - data[0].starting_balance) / data[0].starting_balance) * 100
            context['percent_change'] = percent_change

        return render(request, 'registration/my_account.html', context)


