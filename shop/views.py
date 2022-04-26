from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    # products= Product.objects.all()
    # n= len(products)
    # nSlides= n//4 + ceil((n/4)-(n//4))
    # allProds=[[products, range(1, nSlides), len(products)],
    #           [products, range(1, nSlides), len(products)]]
    
    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return HttpResponse("We are at about")

def search(request):
    return HttpResponse("We are at about")

def productView(request):
    return HttpResponse("We are at about")

def checkout(request):
    return HttpResponse("We are at about")