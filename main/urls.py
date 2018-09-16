from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    
    path('products/', product_list, name='products'),
    path('product/<slug:slug>/', product_detail, name='product'),
    path('like/product/<slug:slug>/', like_product, name='like'),

    path('categories/', CategoryListView.as_view(), name='categories'),
    path('category/<slug:slug>/', category_detail, name='category'),

    path('search/', search, name='search'),
]