from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_to_all_users(subject,message,email_list):
    result = send_mail(subject,message, 'azamovshahboz06082001@gmail.com', email_list)
    return result