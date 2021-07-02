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


