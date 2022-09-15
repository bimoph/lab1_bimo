from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Bimo Priyohutomo'
    }
    return HttpResponse(serializers.serialize("xml", data_barang_wishlist), content_type="application/xml")

def show_wishlistjson(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Bimo Priyohutomo'
    }
    return HttpResponse(serializers.serialize("json", data_barang_wishlist), content_type="application/json")

def show_filter(request,id):
    data = BarangWishlist.objects.filter(pk=id)
    # // Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    # // Jika XML
