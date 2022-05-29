from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.index, name='home'),
    path('images/',views.images,name='images'),
    path('search/', views.search_results, name='search_results'),
    path('location/',views.get_location,name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)