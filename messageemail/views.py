
from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


class Home(FormView):
    template_name = 'messageemail/home.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    