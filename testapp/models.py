from django.db import models

# Create your models here.
class HydJobs(models.Model):

    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phonenumber = models.IntegerField()

class BloreJobs(models.Model):

    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phonenumber = models.IntegerField()

class ChennaiJobs(models.Model):

    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phonenumber = models.IntegerField()

class PuneJobs(models.Model):

    date = models.DateField()
    company = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
