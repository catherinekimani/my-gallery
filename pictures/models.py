from distutils.command.upload import upload
from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=40)
    image_description = models.TextField(max_length=60)
    image = models.ImageField(upload_to = 'pictures')
    date_posted = models.DateTimeField(auto_now_add=True)
    
class Category(models.Model):
    name = models.CharField(max_length=60)
    
class Location(models.Model):
    name = models.CharField(max_length=60)