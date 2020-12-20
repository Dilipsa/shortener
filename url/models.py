from django.db import models

class UrlData(models.Model):
    url = models.CharField(max_length=800)
    slug = models.CharField(unique=True, max_length=15)
    domain = models.CharField(max_length=800, null=True)
    
    def __str__(self):
            return self.url

    def get_short_url(self):
        return f"{self.domain}{self.slug}"