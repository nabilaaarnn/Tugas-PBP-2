from django.shortcuts import render
from mywatchlist.models import Mywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_mywatchlist(request):
    data_mywatchlist = Mywatchlist.objects.all()
    context = {
        'watchlist' : data_mywatchlist,
        'nama': 'Nabila',
        'npm' : '2106653344'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = Mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Mywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Mywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

