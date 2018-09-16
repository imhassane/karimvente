from django import forms
from accounts.models import Profile
from django.contrib.auth.models import User

class EditUserForm(forms.Form):
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': 'Ex: Malik'
    }), required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': 'Ex: Ftissi'
    }), required=False)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': 'Ex: malik.ftissi@mail.com'
    }), required=False)



class EditProfileForm(forms.ModelForm):

    error_css_class = 'uk-form-error'
    required_css_class = 'uk-form-error'

    class Meta:
        model = Profile
        fields = '__all__'