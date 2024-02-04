# search_app/urls.py
from django.urls import path
from .views import searchrelt

app_name = "search_app"

urlpatterns = [
    path('', searchrelt, name='searchrelt'),
]
