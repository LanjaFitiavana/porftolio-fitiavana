from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf  import settings
from django.contrib import messages


class Home(FormView):
    template_name = 'messageemail/home.html'
    form_class = ContactForm
    success_url = reverse_lazy ('home')

    def form_valid(self,form):
        message_instance = form.save()
        nom = message_instance.nom
        email_exp = message_instance.email
        contenu = message_instance.contenu
        
        contenu_email = f"""
        Nom:{nom}
        Email:{email_exp}
        Message:{contenu}
        """
        try:
            send_mail(
                subject=f"nouveau message de :{nom}",
                message=contenu_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.MON_EMAIL_DE_RECEPTION],
                fail_silently=False,
                
                
            )
            print(f"Bien envoyer")
            messages.success(self.request,"Votre message a été envoyé avec succès !")
        except Exception as e:
            print(f"erreur d'envoie:{e}")
            messages.error(self.request,"Erreur de l'envoie de l'email.Veuillez resayer   s'il vous plait.")

        return super().form_valid(form)
     #a propos


    


