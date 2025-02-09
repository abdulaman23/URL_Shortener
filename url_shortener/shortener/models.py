from django.db import models

import shortuuid
# Create your models here.

class URL(models.Model):
    short_url = models.CharField(max_length=10, unique=True, primary_key=True)
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortuuid.uuid()[:8]
        super().save(*args,**kwargs)

    
    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"