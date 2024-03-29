# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        message = 'Thank you for registering on our website. We hope you enjoy your stay!'
        from_email = 'azamovshahboz06082001@gmail.com'  # Replace with your email
        to_email = instance.email
        send_mail(subject, message, from_email, [to_email])
