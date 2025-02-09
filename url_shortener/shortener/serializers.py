from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):

    short_url = serializers.CharField(read_only=True)
    class Meta:
        model = URL
        fields = ['short_url', 'long_url']

