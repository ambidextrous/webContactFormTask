#u-*- coding: utf-8 -*-
from __future__ import unicode_literals
import threading
from django.core.mail import send_mail, BadHeaderError, mail_admins
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def sendEmails(name, email, message):
    """
    Send confirmation emails to user and admin
    """
    try:
        # Send automatic confirmation email to user
        messageToUser = 'Dear ' + name + ',\n\n Thanks for your interest in Beeks Financial Cloud and for your message:\n\n\"' + message + '\"\n\n  We will review your message and get back in contact with you within one working day,\n\n  The Beeks Customer Service team'
        send_mail('Message received confirmation', messageToUser, 'customerservice@beeksfinancialcloud.com', [email], fail_silently=True)
        # Send automatic email to all ADMINs in settings.py
        messageToAdmin = 'Contact name: ' + name + '\n\nContact email: ' + email + '\n\nContact message: ' + message
        mail_admins('New Contact Message', messageToAdmin, fail_silently=True)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def email(request):
    """
    Web contact form view
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save user data to database
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Sends emails on new thread to speed up user experience 
            t = threading.Thread(target=sendEmails, args=(name, email, message,))
            t.start()
            return redirect('success')
    return render(request, 'email.html', {'form': form})


def success(request):
    """
    'Thank you' message view
    """
    return render(request, 'success.html')
