from django.db import models
from django.forms import CharField
from django.db import models








class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    # image = models.ImageField(upload_to= 'base_app/images/')
    url = models.URLField(blank= True) 

    def __str__(self):
        return self.title


class Ipmodel(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip