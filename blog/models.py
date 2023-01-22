from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_description = models.TextField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='blog/')
    is_published = models.BooleanField(default=False)
