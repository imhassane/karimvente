from django import forms
from django.core.mail import send_mail


class MailForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input border border-secondary'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'uk-input border border-secondary'
    }))

    objet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input border border-secondary'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'uk-input border border-secondary',
        'row': '4'
    }))

    def send_mail(self, subject, sender, message):

        subject = subject
        sender = sender
        message = message
        recipient_list = ['imthassane@gmail.com']

        html_message = "\
            <div>\
                <p><strong>Ce mail a été envoyé par {from_email}</strong></p>\
                <p>{message}</p>\
            </div>\
        ".format(from_email=sender, message=message)

        send_mail(html_message=html_message, subject=subject, message=message, from_email=sender, recipient_list=recipient_list)
