from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate as auth, login
from accounts.forms import LoginForm

from django.contrib.auth.decorators import user_passes_test
from .decorators import user_not_authenticated


@user_passes_test(user_not_authenticated, login_url='/', redirect_field_name=None)
def signin(request):

    context = {}

    form = LoginForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = auth(request, username=username, password=password)
        
        if user:
            login(request, user)

            return redirect(reverse('main:home'))

    return render(request, "login.html", context)