from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.
class Profile(models.Model):
    profile_pic=CloudinaryField('image')
    fullname=models.CharField(max_length=100)
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user
    
    @classmethod
    def search_profile(cls, fullname):
        return cls.objects.filter(user__username__icontains=fullname).all()
    
    @receiver(post_save,sender=User)
    def createUserProfile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def saveUserProfile(sender, instance, **kwargs):
        instance.profile.save()
    def saveProfile(self):
        self.user()
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length =100)
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='images', null=True)
    
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    class Meta:
        ordering = ['-date_posted']
        
class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    date_comment = models.DateTimeField(auto_now_add=True)
    comments=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.comments
class Likes(models.Model):
    image = models.ForeignKey(Image,related_name='like_count', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.image