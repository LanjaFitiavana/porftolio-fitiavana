from django import forms
from .models import MessageEmail

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageEmail
        fields = ['nom','email','contenu']
        widgets = {
            'nom':forms.TextInput(attrs = {
                'placeholder':'votre nom',
                'class':'in'
            }),
            'email':forms.EmailInput(attrs = {
                'placeholder':'votre email',
                'class':'in'
            }),           
            'contenu':forms.Textarea(attrs = {
                'placeholder':'votre message',
                
            }),
        }