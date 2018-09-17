from django.shortcuts import render
from trades.models import Trades
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def get_data(request):
    trades = Trades.objects.filter(user_id=request.user.id)
    return JsonResponse(list(trades.values()), safe=False)

def index(request):
    return render(request, 'charts/charts.html')