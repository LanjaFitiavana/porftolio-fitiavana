from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from smtplib import SMTPException
from django.conf import settings
from django.contrib import messages
import logging

# Configurer le logging pour voir les détails SMTP
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Home(FormView):
    template_name = 'messageemail/home.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        message_instance = form.save()

        nom = message_instance.nom
        email_exp = message_instance.email
        contenu = message_instance.contenu

        contenu_email = (
            f"Nom : {nom}\n"
            f"Email : {email_exp}\n"
            f"Message :\n{contenu}"
        )

        try:
            send_mail(
                subject=f"Nouveau message de : {nom}",
                message=contenu_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.MON_EMAIL_DE_RECEPTION],
                fail_silently=False,
                timeout=getattr(settings, 'EMAIL_TIMEOUT', 10)
            )
            logger.info(f"Email envoyé avec succès à {settings.MON_EMAIL_DE_RECEPTION}")
            messages.success(self.request, "Votre message a été envoyé avec succès !")
        except BadHeaderError as e:
            logger.error(f"BadHeaderError: {e}")
            messages.error(self.request, "Erreur: mauvais en-tête dans l'email.")
        except SMTPException as e:
            logger.error(f"Erreur SMTP: {e}")
            messages.error(self.request, f"Erreur SMTP: {e}")
        except Exception as e:
            logger.error(f"Erreur inconnue lors de l'envoi de l'email: {e}")
            messages.error(self.request, f"Erreur lors de l'envoi de l'email: {e}")

        return super().form_valid(form)
