from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.

    
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='images', blank =False, null = True)
    Bio = models.TextField(max_length=1500)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.Bio
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.objects.filter(id = id).update(bio =bio)
        return update_profile
    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains = user).all()
        
class Picture(models.Model):
    image = models.ImageField(upload_to = 'post/',blank = False, null = True)
    image_name = models.CharField(max_length = 100)
    image_caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length = 1500)
    
    