from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):

    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Muhammad Adryan Haska Putra',
    'npm': '2106750641',
    }

    return render(request, "katalog.html", context)