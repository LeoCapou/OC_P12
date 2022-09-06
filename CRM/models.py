from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_sales = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)


class Sales_Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sales_contact",
    )


class Support_Contact(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="support_contact",
    )


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    sales_contact = models.ForeignKey(
        Sales_Contact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="clients",
    )
    support_contact = models.ForeignKey(
        Support_Contact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="clients",
    )


class Contrat(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()
    sales_contact = models.ForeignKey(
        Sales_Contact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="contrats",
    )
    client = models.ForeignKey(
        Client,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="contrats",
    )


class Event(models.Model):
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(null=True, blank=True)
    contrat = models.OneToOneField(
        Contrat,
        on_delete=models.CASCADE,
        related_name="event",
    )
    support_contact = models.ForeignKey(
        Support_Contact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="events",
    )
    sales_contact = models.ForeignKey(
        Sales_Contact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="events",
    )
