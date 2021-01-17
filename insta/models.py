from django.db import models

# Create your models here.
class Picture(models.Model):
    image = ImageField(upload_to = 'post/',blank = False, null = True)
    image_name = model.CharField(max_length = 100)
    image_caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length = 1500)
    
class Profile(models.Model):
    profile_photo = models.ImageField()
    Bio = models.TextField(max_length=1500)
    
    