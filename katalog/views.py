from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_catalog(request):
    data_catalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_catalog,
        'nama': 'Nabila',
        'npm' : '2106653344'
    }
    print(data_catalog)
    return render(request, "katalog.html", context)

