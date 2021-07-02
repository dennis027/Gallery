from django.db import models

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

    def __str__(self):
        return self.name

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
     image = models.ImageField(max_length=255)
     description = models.CharField(max_length=255)
     
     location = models.ForeignKey(Location,on_delete=models.CASCADE)
     category = models.ForeignKey(Category,on_delete=models.CASCADE)

   


     def __str__(self):
         return self.image

     def save_delete(self):
        self.save()

     def delete_delete(self):
        self.delete()
            
    



     


