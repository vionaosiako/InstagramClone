from django.contrib import admin

from .models import Profile,Image,Likes,Comment
# Register your models here.
admin.site.register(Profile),
admin.site.register(Image),
admin.site.register(Likes),
admin.site.register(Comment),