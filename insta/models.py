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
    image = models.ImageField(upload_to = 'images/',blank = False, null = True)
    image_name = models.CharField(max_length = 100)
    image_caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length = 1500)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_caption(self,caption):
        updated_cap = cls.objects.filter(id = id).update(caption = caption)
        return updated_cap
    
    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image
    
    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(user__name__icontains = name)
        return profile
    
    @classmethod
    def get_one_image(cls,name):
        image = cls.objects.get(pk = id)
        return image
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['-date_uploaded']
    
class Comments(models.Model):
    comment = models.CharField(max_length = 50, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
        
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments


    def __str__(self):
        return self.comment
