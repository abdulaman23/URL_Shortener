from django.urls import path
from .views import shorten_url, get_long_url

urlpatterns = [

    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/',get_long_url,name='get_long_url'),
]