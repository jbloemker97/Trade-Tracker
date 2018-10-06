from django.shortcuts import render
from trades.models import Trades
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Max
from user.models import Profile


@login_required
def get_data(request):
    trades = Trades.objects.filter(user_id=request.user.id).order_by('exit_date')
    return JsonResponse(list(trades.values()), safe=False)

def get_max_pnl(request):
    max_trade = Trades.objects.filter(user_id=request.user.id).aggregate(Max('pnl'))
    return JsonResponse(max_trade, safe=False)

def index(request):
    trades = Trades.objects.filter(user_id=request.user.id).order_by('id')[:4]
    context = {
        'trades': trades
    }
    return render(request, 'charts/charts.html', context)

def get_future_pnl(request):
    user = Profile.objects.select_related('user_id').all()
    return JsonResponse(list(user.values()), safe=False)