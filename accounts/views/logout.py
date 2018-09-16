from django.contrib.auth.decorators import user_passes_test
from .decorators import user_is_authenticated
from django.contrib.auth import logout
from django.shortcuts import redirect, reverse


@user_passes_test(user_is_authenticated)
def signout(request):
    logout(request)
    
    return redirect(reverse('main:home'))
