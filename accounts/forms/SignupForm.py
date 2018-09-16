from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile


class SignupForm(forms.Form):

    error_css_class = 'uk-form-error'
    required_css_class = 'uk-form-error'

    auto_id = True

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: alpha22"
    }), error_messages={
        'required': "Veuillez entrer un nom d'utilisateur"
    })

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: alpha22@gmail.com"
    }), error_messages={
        'required': "Veuillez entrer une adresse email"
    })

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: warrior-fan164"
    }), error_messages={
        'required': "Veuillez entrer un mot de passe"
    })

    rptpassword = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: warrior-fan164"
    }), error_messages={
        'required': "Vos mots de passe doivent correspondre"
    })

    def clean(self):
        
        cleaned_data = super().clean()

        username, email = cleaned_data['username'], cleaned_data['email']
        password, rptpassword = cleaned_data['password'], cleaned_data['rptpassword']

        if password != rptpassword:
            raise forms.ValidationError("Les deux mots de passe doivent être identiques")
        
        else:
            
            # On enregistre un nouvel utilisateur
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # On crée son profil.
            profil = Profile(user=user, avatar='default.jpg')
            profil.save()
        
        return cleaned_data
