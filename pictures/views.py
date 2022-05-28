from unicodedata import category
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category,Location,Image
# Create your views here.
def index(request):
    return render(request, 'index.html')

def images(request):
    images = Image.objects.all()
    category = Category.objects.all()
    location = Location.objects.all()
    return render(request,'images.html',{'images':images,'category':category,'location':location})
