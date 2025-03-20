from django.urls import path
from ..Views import empresaView
from django.shortcuts import render

urlpatterns = [
   
    path('empresa/', empresaView.empresa_list),
    path('empresa/<int:id>',empresaView.empresa_get),
    path('empresa/create',empresaView.empresa_create),
    path('empresa/update/<int:id>',empresaView.empresa_update),
    path('empresa/delete/<int:id>',empresaView.empresa_delete), 

]