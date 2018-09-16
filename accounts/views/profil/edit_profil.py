from django.core.files.storage import FileSystemStorage
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 as _g

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from accounts.views.decorators import user_is_authenticated, user_not_authenticated

from accounts.forms import EditProfileForm, EditUserForm
from accounts.models import Profile
from django.views.generic.edit import UpdateView

from karimvente.functions import handle_upload_file


@user_passes_test(user_is_authenticated)
def change_first_name(request):

    user = request.user
    first_name = request.GET['first_name']

    user.first_name = first_name
    user.save()

    return JsonResponse({'first_name': first_name})


@user_passes_test(user_is_authenticated)
def change_last_name(request):

    user = request.user
    last_name = request.GET['last_name']

    user.last_name = last_name
    user.save()

    return JsonResponse({'last_name': last_name})


@user_passes_test(user_is_authenticated)
def change_email(request):

    user = request.user
    email = request.POST.get('email', '')

    user.email = email
    user.save()

    return JsonResponse({'email': email})


@user_passes_test(user_is_authenticated)
def delete_account(request):

    user = request.user

    user.is_active = False
    user.save()

    return JsonResponse({'is_active': user.is_active})


@user_passes_test(user_not_authenticated)
def activate_account(request):
    
    return render(request, "edit_profil.html")
    

@user_passes_test(user_is_authenticated)
def edit_profil(request):
    
    context = {}
    user = request.user

    # Valeurs par défaut des formulaires.
    user_form_initial = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }

    # Formulaire d'édition de l'utilisateur.
    user_form = EditUserForm(request.POST or None, initial=user_form_initial)
    context['user_form'] = user_form

    if user_form.is_valid():
        
        first, last = user_form.cleaned_data['first_name'], user_form.cleaned_data['last_name']
        email = user_form.cleaned_data['email']

        if len(first) != 0:
            user.first_name = first
        
        if len(last) != 0:
            user.last_name = last

        if len(email) != 0:
            user.email = email
        
        user.save()
    
    # Formulaire d'édition du profil
    profil = _g(Profile, user=user)
    profil_form = EditProfileForm(request.POST, request.FILES, initial={'avatar': profil.avatar})
    context['profil_form'] = profil_form

    if profil_form.is_valid():
        file_name = profil_form.cleaned_data['avatar']

        handle_upload_file('users', file_name, request.FILES)
        profil.avatar = file_name
        profil.save()
    
    return render(request, "edit_profil.html", context)

