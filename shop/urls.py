from django.contrib import admin
from django.urls import path
 
from shop.views import CategoryAPIView
 
urlpatterns = [
    path('api/category/', CategoryAPIView.as_view())
]