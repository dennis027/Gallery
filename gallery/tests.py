from gallery.models import Image,Poster,Location,Category
from django.test import TestCase

# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.new = Image(title='new',description='i downloaded',date='')

    def test_instances(self):
        self.assertTrue(isinstance(self.new,Image))    

    #testing save method
    def test_save_method(self):
        self.new.save_image()
        image = Image.objects.all()
        self.assertTrue(len(Image)>0)


