# app/urls.py
from django.urls import path
from .views import allProduct, productdet, products_by_category

app_name = "shop"

urlpatterns = [
    path('', allProduct, name='allProduct'),
    path("<slug:c_slug>/", products_by_category, name="Product_by_cat"),
    path("<slug:c_slug>/<slug:product_slug>/", productdet, name="Productcatdet"),
]
