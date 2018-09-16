from django.shortcuts import render, redirect, reverse
from accounts.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .decorators import user_not_authenticated


@user_passes_test(user_not_authenticated, login_url='/', redirect_field_name=None)
def signup(request):

    context = {}

    form = SignupForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        
        # On connecte l'utilisateur
        user = authenticate(request,\
            username=form.cleaned_data['username'], \
            password=form.cleaned_data['password'])
        
        if user:
            login(request, user)

            return redirect(reverse('main:home'))

    return render(request, "signup.html", context)