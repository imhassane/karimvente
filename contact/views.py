from django.shortcuts import render
from .forms import MailForm

# Create your views here.
def contact_home(request):

    context = {}
    mailform = MailForm(request.POST or None)

    context['mailform'] = mailform

    if mailform.is_valid():

        subject = mailform.cleaned_data['objet']
        sender = mailform.cleaned_data['email']
        message = mailform.cleaned_data['message']

        mailform.send_mail(sender=sender, subject=subject, message=message)

        context['mail_success'] = True


    return render(request, 'contact.html', context)
