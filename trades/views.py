from django.shortcuts import render, get_object_or_404
from .forms import EntryForm
from .models import Trades
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
import datetime
from django.urls import reverse
import csv
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    form = EntryForm()
    trades = Trades.objects.filter(user_id=request.user.id)
    return render(request, 'trades/index.html', {'trades': trades, 'form': form})
   


def trades(request):
    if request.method == 'GET':
        form = EntryForm()

    elif request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            position = form.cleaned_data['position']
            shares = form.cleaned_data['shares']
            entry_date = form.cleaned_data['entry_date']
            exit_date = form.cleaned_data['exit_date']
            entry_price = form.cleaned_data['entry_price']
            exit_price = form.cleaned_data['exit_price']
            pnl = form.cleaned_data['pnl']
            entry_comments = form.cleaned_data['entry_comments']
            exit_comments = form.cleaned_data['exit_comments']

            Trades.objects.create(
                user_id=request.user.id,
                ticker=ticker,
                position=position,
                shares=shares,
                entry_date=entry_date,
                exit_date=exit_date,
                entry_price=entry_price,
                exit_price=exit_price,
                pnl=pnl,
                entry_comments=entry_comments,
                exit_comments=exit_comments
            ).save()

            return HttpResponseRedirect(reverse("trades:index"))

    return render(request, 'trades/form.html', {'form': form})

def delete_trade(request, pk):
    if request.method == 'DELETE':
        trade = get_object_or_404(Trades, pk=pk)
        trade.delete()

    return HttpResponse(status=200)

def update_trade(request, pk):
    if request.is_ajax():
        id = request.POST.get('id', '')
        trade = Trades.objects.filter(pk=id).update(
            ticker=request.POST.get('ticker'),
            position=request.POST.get('position'),
            shares=request.POST.get('shares'),
            entry_date=datetime.datetime.strptime(request.POST.get('entry_date'), '%m/%d/%y').date(),
            exit_date=datetime.datetime.strptime(request.POST.get('exit_date'), '%m/%d/%y').date(),
            entry_price=request.POST.get('entry_price'),
            exit_price=request.POST.get('exit_price'),
            pnl=request.POST.get('pnl'),
            entry_comments=request.POST.get('entry_comments'),
            exit_comments=request.POST.get('exit_comments')
        )
    return HttpResponse(status=200)

def csv_write(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=trades.csv'
    writer = csv.writer(response)
    trades = Trades.objects.filter(user_id=request.user.id)

    writer.writerow(['Ticker', 'Position', 'Shares', 'Entry Date', 'Exit Date', 'Entry Price', 'Exit Price', 'PnL', 'Entry Comments', 'Exit Comments'])

    for trade in trades:
        writer.writerow([trade.ticker, trade.position, trade.shares, trade.entry_date, trade.exit_date, trade.entry_price, trade.exit_price, trade.pnl, trade.entry_comments, trade.exit_comments])

    
    return response