from django.db import models

# Create your models here.

from datetime import date
from django.utils import timezone
from ckeditor.fields import RichTextField

class ContactRequest(models.Model):
    full_name               = models.CharField(verbose_name='Full Name',max_length=255)
    email                   = models.EmailField(verbose_name='Email Address',max_length=255)
    phone                   = models.CharField(max_length=15)
    message                 = models.TextField()
    date_contacted          = models.DateTimeField(auto_now_add=True)
    date_review             = models.DateTimeField(blank=True,null=True)
    

    class Meta:
        verbose_name = ("Contact Request")
        verbose_name_plural = ("Contact Requests")
        ordering            = ("-date_review",)

    def __str__(self):
        return self.full_name


# Email newsletter 

class Subscriber(models.Model):

    email                       = models.EmailField()
    date_subscribed             = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Subscriber")
        verbose_name_plural = ("Subscribers")

    def __str__(self):
        return self.email


class MailMessage(models.Model):

    title                   = models.CharField(max_length=255)
    message                 = models.TextField()
    date_messaged           = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Mail Message")
        verbose_name_plural = ("Mail Messages")

    def __str__(self):
        return self.title