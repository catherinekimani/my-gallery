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

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET["category"]
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})
    return render(request,'search.html')

def get_location(request,location_id):
    images=Image.filter_by_location(location_id)
    return render(request, 'location.html', {"images":images})