from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime as dt
from ckeditor.fields import RichTextField

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=40)
    image_description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'pictures/')
    date_posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,null=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    def update_image(self,image_name,image_description,image,date_posted):
        self.image_name = image_name
        self.image_description = image_description
        self.image = image
        self.date_posted = date_posted
    
    @classmethod
    def filter_by_location(cls, location):
        location = Image.objects.filter(location__name=location).all()
        return location
    
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(category__name=search_term)
        return category
    
    def __str__(self):
        return self.image_name
    
class Category(models.Model):
    name = models.CharField(max_length=60)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    @classmethod
    def get_all_category(cls):
        categories = Category.objects.all()
        return categories
    
    def update_category(self,name):
        self.name = name
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=60)
    
    def save_location(self):
        self.save()
        
    def delete_clocation(self):
        self.delete()
    
    def update_location(self,name):
        self.name = name
        
    def __str__(self):
        return self.name