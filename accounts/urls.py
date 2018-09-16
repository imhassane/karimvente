from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signin/', signin, name='login'),
    path('signup/', signup, name="signup"),
    path('signout/', signout, name='signout'),

    path('edit/firstname/', change_first_name, name='change_first_name'),
    path('edit/lastname/', change_last_name, name='change_last_name'),

    path('edit/', edit_profil, name='edit_profil'),
    path('delete/', delete_account, name='delete_profil'),
    path('profil/', view_profil, name='view_profil'),
]