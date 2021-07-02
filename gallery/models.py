from django.db import models

# Create your models here.

class Poster(models.Model):
    first_name = models.CharField(max_length=255 ,primary_key = True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.first_name



class Location(models.Model):
    name = models.CharField(max_length=255,primary_key = True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255,primary_key = True) 

    def __str__(self):
        return self.name   

class Image(models.Model):
     image = models.ImageField(max_length=255)
     title = models.CharField(max_length=255,primary_key = True) 
     description = models.CharField(max_length=255)
     date = models.CharField(max_length=255,null=True)
     location = models.ForeignKey(Location,on_delete=models.CASCADE)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)

   


     def __str__(self):
         return self.image

     def save_image(self):
        self.save()




     


