from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.

def show_mywatchlist(request):
    data_mywatchList = MyWatchList.objects.all()
    context = {
        'watchlist' : data_mywatchlist,
        'nama': 'Nabila',
        'npm' : '2106653344'
    }
    print(data_mywatchlist)
    return render(request, "mywatchlist.html", context)

