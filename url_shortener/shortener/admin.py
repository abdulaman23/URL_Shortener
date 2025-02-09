from django.contrib import admin
from .models import URL

# Register your models here.


class URLAdmin(admin.ModelAdmin):
    list_display = ('short_url', 'long_url', 'created_at')

admin.site.register(URL, URLAdmin)
admin.site.site_header = "URL Shortener Admin"
