from django.urls import path
from .views import home, shorten_url, get_long_url

urlpatterns = [

    path('', home, name='home'),
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/',get_long_url,name='get_long_url'),
]