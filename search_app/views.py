# search_app/views.py
from django.shortcuts import render
from app.models import Product
from django.db.models import Q

def searchrelt(request):
    Products = None
    query = None
    if "q" in request.GET:
        query = request.GET.get("q")
        Products = Product.objects.filter(Q(name__icontains=query) | Q(des__icontains=query))

    return render(request, "search.html", {"query": query, "products": Products})
