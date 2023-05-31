from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='home'),
    path('images/',views.images,name='images'),
    path('search/', views.search_results, name='search_results'),
    path('location/',views.get_location,name='location'),
]
