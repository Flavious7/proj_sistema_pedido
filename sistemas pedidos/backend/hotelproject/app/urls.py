from django.urls import path, include
from . import views
from django.shortcuts import render

urlpatterns = [

  
    path('',include('app.Urls.empresaUrl')),
    path('',include('app.Urls.pedidoUrls')),
    
    
]