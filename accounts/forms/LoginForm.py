from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: alpha22"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': 'Ex: warrior-fan164'
    }))
