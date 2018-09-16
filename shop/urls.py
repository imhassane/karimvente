from django.urls import path
from .views import *

app_name = 'shop'
urlpatterns = [
    path('new/order/<int:product_pk>/', add_to_bucket, name='add_to_bucket'),
    path('remove/order/<int:order_pk>/', del_from_bucket, name='remove_order'),

    path('bucket/validate/', validate_order, name='validate_bucket'),
    path('buckets/list/', show_orders, name='show_buckets'),
    
    path('', bucket, name='bucket'),
]