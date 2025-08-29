from django.urls import path

from . import views

urlpatterns = [
    path('', views.loja),
    path('carrinho/', views.carrinho),
]
