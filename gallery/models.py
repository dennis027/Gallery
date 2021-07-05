from django.db import models
import pyperclip
# Create your models here.

class Poster(models.Model):
    first_name = models.CharField(max_length=255 ,primary_key = True)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    def save_poster(self):
        self.save()

    def delete_poster(self):
        self.delete()



class Location(models.Model):
    name = models.CharField(max_length=255,primary_key = True)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)    

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
                

class Category(models.Model):
    name = models.CharField(max_length=255,primary_key = True) 

    def __str__(self):
        return self.name   
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
                    

class Image(models.Model):
     name = models.CharField(max_length=255,primary_key = True) 
     image = models.ImageField(upload_to='media/')
     description = models.CharField(max_length=255) 
     location = models.ForeignKey(Location,on_delete=models.CASCADE)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)


    
     @classmethod
     def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

     @classmethod
     def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

     @classmethod
     def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

     @classmethod
     def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images


     def save_image(self):
        self.save()

     def delete_image(self):
        self.delete()

    
    



     


