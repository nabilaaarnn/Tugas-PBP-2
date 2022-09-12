from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_catalog(request):
    data_catalog = CatalogItem().objects.all()
    data_catalog = {
        'list_katalog': data_catalog,
        'nama': 'Nabila',
        'npm' : '2106653344'
    }

    return render(request, "katalog.html", context)

