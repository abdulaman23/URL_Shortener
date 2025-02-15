from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import URL
from .serializers import URLSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect,JsonResponse


def home(request):
    """Home page rendering view"""

    return render (request, "shortener/index.html")

@api_view(['POST'])
def shorten_url(request):

    """API to shorten a URL"""

    serializer = URLSerializer(data=request.data)
    
    if serializer.is_valid():
        url = serializer.save()

        return Response({"short_url":url.short_url,"long_url":url.long_url},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['GET'])
def get_long_url(request, short_url):

    """Redirect to the original URL"""

    url = get_object_or_404(URL, short_url=short_url)

    '''if request.headers.get('Accept') == 'application/json':
        return JsonResponse({"long_url": url.long_url})
    
    return HttpResponseRedirect(url.long_url)'''

    return JsonResponse({"long_url": url.long_url})

