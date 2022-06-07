from django.test import TestCase
from .models import Image,Profile
from django.contrib.auth.models import User


# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        
        self.user = User(username='riziki') 
        self.user.save()
        self.profile=Profile(user=self.user,fullname='viona',bio='Its me',profile_pic='')
        
        
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username='riziki') 
        self.user.save()
        self.profile=Profile(user=self.user,fullname='viona',bio='Its me',profile_pic='')
        self.image=Image(id=1,image='',name='book', caption='Its amazing', date_posted='', user=self.profile)
        
    def tearDown(self):
        User.objects.all().delete()
        Image.objects.all().delete()
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
    
    def test_save_image(self):
        saved_image=Image.objects.all().delete()
        self.assertTrue((len(saved_image))>0)
        
    def test_delete_image(self):
        self.image.delete_image()
        delete_image=Image.objects.all()
        self.assertTrue(len(delete_image)==0)
    