from django.shortcuts import render
from .forms import EntryForm

def index(request):
    return render(request, 'trades/index.html')


def trades(request):
    if request.method == 'GET':
        form = EntryForm()

    return render(request, 'trades/form.html', {'form': form})