from gallery.models import Image,Poster,Location,Category
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
import pyperclip
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.new = Image(name='new',description='i downloaded')

    def test_instances(self):
        self.assertTrue(isinstance(self.new,Image))    

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'MEDIA/test.jpg')
        changed_img = Image.objects.filter(image='MEDIA/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
    

    
    # def test_copy_image(self):
    #     '''
    #     Test to confirm that we are copying image link
    #     '''

    #     self.new_image.save_image()
    #     Image.copy_link("www.com")

    #     self.assertEqual(self.new_image.link,pyperclip.paste())    

    # testing save method
    # def test_save_method(self):
    #     self.new.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(Image)>0)
    
    # def test_delete_method(self):
    #     self.new.save_image()
    #     image = Image.objects.all()
    #     self.new.delete_image()
    #     self.assertTrue(len(image)==0)

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
