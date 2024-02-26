from django.db import models

# Create your models here.

class CategoryDB(models.Model):
    NAME = models.CharField(max_length=100, null=True, blank=True)
    DESC = models.CharField(max_length=100, null=True, blank=True)
    IMAGE = models.ImageField(upload_to='Images', null=True, blank=True)

class ProdcutDB(models.Model):
    CATEGORY = models.CharField(max_length=100, null=True, blank=True)
    PRONAME = models.CharField(max_length=100, null=True, blank=True)
    PROPRICE = models.IntegerField(null=True, blank=True)
    PRODESC = models.CharField(max_length=100, null=True, blank=True)
    PROIMAGE = models.ImageField(upload_to='Images', null=True, blank=True)

class BlogDB(models.Model):
    DATE = models.DateField(null=True, blank=True)
    TITLE = models.CharField(max_length=100, null=True, blank=True)
    SHORTDESC = models.CharField(max_length=200, null=True, blank=True)
    FULLDESC = models.CharField(max_length=800, null=True, blank=True)
    IMAGE = models.ImageField(upload_to='Images', null=True, blank=True)