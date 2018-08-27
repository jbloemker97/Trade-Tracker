from django.shortcuts import render, get_object_or_404
from .forms import EntryForm
from .models import Trades
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import UpdateView
import datetime
from django.urls import reverse

def index(request):
    form = EntryForm()
    trades = Trades.objects.all()
    return render(request, 'trades/index.html', {'trades': trades, 'form': form})


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
            entry_date=datetime.datetime.strptime(request.POST.get('entry_date'), '%m/%d/%y').date(),
            exit_date=datetime.datetime.strptime(request.POST.get('exit_date'), '%m/%d/%y').date(),
            entry_price=request.POST.get('entry_price'),
            exit_price=request.POST.get('exit_price'),
            pnl=request.POST.get('pnl'),
            entry_comments=request.POST.get('entry_comments'),
            exit_comments=request.POST.get('exit_comments')
        )
    return HttpResponse(status=200)
