from django.shortcuts import render, get_object_or_404
from .forms import EntryForm
from .models import Trades
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    trades = Trades.objects.all()
    return render(request, 'trades/index.html', {'trades': trades})


def trades(request):
    if request.method == 'GET':
        form = EntryForm()

    elif request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            entry_date = form.cleaned_data['entry_date']
            exit_date = form.cleaned_data['exit_date']
            entry_price = form.cleaned_data['entry_price']
            exit_price = form.cleaned_data['exit_price']
            pnl = form.cleaned_data['pnl']
            entry_comments = form.cleaned_data['entry_comments']
            exit_comments = form.cleaned_data['exit_comments']

            Trades.objects.create(
                ticker=ticker,
                entry_date=entry_date,
                exit_date=exit_date,
                entry_price=entry_price,
                exit_price=exit_price,
                pnl=pnl,
                entry_comments=entry_comments,
                exit_comments=exit_comments
            ).save()

            return HttpResponseRedirect('/')

    return render(request, 'trades/form.html', {'form': form})

def delete_trade(request, pk):
    if request.method == 'DELETE':
        trade = get_object_or_404(Trades, pk=pk)
        trade.delete()

    return HttpResponse(status=200)