import datetime
from datetime import time

from django.db import models
from django.db.models import Model, DateTimeField, EmailField, CharField, TextField

from .tasks import send_email_to_all_users
# Create your models here.

class CreatedBaseModel(Model):
    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(CreatedBaseModel):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    RATE_CHOICES = [(i / 10, str(i / 10)) for i in range(0, 51)]
    CATEGORY_CHOICES = (
        ('Web Designer', 'Web Designer'),
        ('Graphic Designer', 'Graphic Designer'),
        ('PHP Developer', 'PHP Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Banking', 'Banking'),
        ('Accountancy', 'Accountancy'))

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='NONE')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    rate = models.DecimalField(max_digits=3, decimal_places=1, choices=RATE_CHOICES, default=0.0)
    image = models.ImageField(upload_to='media/users', default='media/default.jpg')
    email = models.EmailField(default='azamovshahboz06082001@gmail.com')

    # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    #     super().save(force_insert, force_update, using, update_fields)
    #     emails: list = Email.objects.values_list('email', flat=True)
    #     # start = time.time()
    #     send_email_to_all_users.delay("Yangi blog qo'shildi", self.name, list(emails))
    #     print(emails)
    #     # end = time.time()
    #     # print(end - start, 's -- ketgan vaqt')

    def __str__(self):
        return self.name


class Email(CreatedBaseModel):
    email = EmailField(max_length=255, unique=True)

    def __str__(self):
        return self.email


class CeleryTaskResult(Model):
    task_id = CharField(max_length=255, unique=True)
    result = TextField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task ID: {self.task_id}"
