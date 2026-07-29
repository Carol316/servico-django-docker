from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_produtos, name='catalogo_produtos'),
]