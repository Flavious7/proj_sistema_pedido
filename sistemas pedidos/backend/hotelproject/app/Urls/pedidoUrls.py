from django.urls import path
from ..Views import pedidoView
from django.shortcuts import render

urlpatterns = [
   
    path('pedido/', pedidoView.pedido_list),
    path('pedido/<int:id>',pedidoView.pedido_get),
    path('pedido/create',pedidoView.pedido_create),
    path('pedido/update/<int:id>',pedidoView.pedido_update),
    path('pedido/delete/<int:id>',pedidoView.pedido_delete), 

]