from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path('profilePage/<int:user_id>', views.profilePage, name='profilePage'),
    path('addNewPost', views.addNewPost, name='addNewPost'),
    path('profileUpdates', views.profileUpdates, name='profileUpdates'),
    path('addNewPost', views.addNewPost, name='addNewPost'),
    path('search_results', views.search_results, name='search_results'),
    path('image/<image_id>/like',views.like_image,name='likeimage'),
    
]