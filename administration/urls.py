from django.urls import path, include
from .views import *

app_name = 'administration'
urlpatterns = [
    path('', adminhome, name='adminhome'),
    path('add/product/', add_product, name='add_product'),
]