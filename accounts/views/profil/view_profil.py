from django.shortcuts import render, get_object_or_404 as _g
from accounts.models import Profile


def view_profil(request):

    profile = _g(Profile, user=request.user)

    return render(request, "view_profil.html", locals())
