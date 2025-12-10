from django.db import models



class MessageEmail(models.Model):
    nom = models.CharField()
    contenu = models.TextField()
    email = models.EmailField()
    date_sms = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
