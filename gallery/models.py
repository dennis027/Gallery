from django.db import models

# Create your models here.

class Poster(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

class image(models.Model):
     image = models.CharField(max_length=255)
     title = models.CharField(max_length=255) 
     description = models.CharField(max_length=255)
     
     