from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Profile(models.Model):
    profile_pic=CloudinaryField('image')
    fullname=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.fullname
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =100)
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_comment = models.DateTimeField(auto_now_add=True)
    comments=models.TextField(null=True)
    def __str__(self):
        return self.comments
class Likes(models.Model):
    image = models.ForeignKey(Image,related_name='like_count', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image