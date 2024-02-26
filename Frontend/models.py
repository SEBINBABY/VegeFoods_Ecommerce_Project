from django.db import models

# Create your models here.

class ContactDB(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(max_length=100, null=True, blank=True)
    SUBJECT = models.CharField(max_length=100, null=True, blank=True)
    MESSAGE = models.CharField(max_length=100, null=True, blank=True)

class UserRegistrationDB(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    EMAIL = models.EmailField(max_length=200, null=True, blank=True, unique=True)
    PASSWORD = models.CharField(max_length=100, null=True, blank=True)

class cartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)

class CheckoutDB(models.Model):
    firstnm = models.CharField(max_length=100, null=True, blank=True)
    lastnm = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)