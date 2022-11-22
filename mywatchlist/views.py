from django.shortcuts import render

# Create your views here.
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

data = MyWatchList.objects.all()

watched = MyWatchList.objects.filter(watched=True).count()
not_watched = MyWatchList.objects.filter(watched=False).count()
message = ''
if (watched > not_watched):
    message = "Selamat, kamu sudah banyak menonton!"
else:
    message = "Wah, kamu masih sedikit menonton!"
    
context = {
    "data_watchlist": data,
    "nama": "Muhammad Adryan Haska Putra",
    "npm": "2106750641",
    "message": message
}

def show_mywatchlist(request):
    return render(request, "root.html", context)

def show_html(request):
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")