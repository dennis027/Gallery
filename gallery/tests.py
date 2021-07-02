from gallery.models import Image,Poster,Location,Category
from django.test import TestCase

# Create your tests here.

# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.new = Image(title='new',description='i downloaded',date='')

#     def test_instances(self):
#         self.assertTrue(isinstance(self.new,Image))    

#     #testing save method
#     def test_save_method(self):
#         self.new.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(Image)>0)


class PosterTestClass(TestCase):
    def setUp(self):
        self.dennis= Poster(first_name ='dennis', last_name='macha',email='dennis@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.dennis, Poster))

    def test_save_method(self):
        self.dennis.save_poster()
        posters = Poster.objects.all()
        self.assertTrue(len(posters)>0)

    def test_delete_method(self):
        self.dennis.save_poster()
        poster = Poster.objects.all()
        self.dennis.delete_poster()
        self.assertTrue(len(poster)==0)



class LocationTestClass(TestCase): 
    def setUp(self):
        self.new_location= Location('Muranga')  
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))   
    def test_save_location(self):
        self.new_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>0)    
    def test_delete_category(self):
        self.new_location.save_location()
        locations= Location.objects.all()
        self.new_location.delete_location()
        self.assertTrue(len(locations)==0)


class CategoryTestClass(TestCase): 
    def setUp(self):
        self.new_category= Category('Picnic')  
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category,Category))   
    def test_save_Category(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)    
    def test_delete_category(self):
        self.new_category.save_category()
        categorys= Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categorys)==0)        
