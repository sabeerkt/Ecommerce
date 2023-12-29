# app/views.py
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import Category, Product

def allProduct(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list, 6)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {"category": c_page, "products": products})

def products_by_category(request, c_slug):
    category = get_object_or_404(Category, slug=c_slug)
    products = Product.objects.filter(category=category, available=True)
    context = {'category': category, 'products': products}
    return render(request, 'category.html', context)

def productdet(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    return render(request, "prdct.html", {"product": product})
