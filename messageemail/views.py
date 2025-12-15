from django.views.generic import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


class Home(TemplateView):
    template_name = 'messageemail/home.html'
    success_url = reverse_lazy('home')

    