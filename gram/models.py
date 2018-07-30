from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    prof_pic = models.ImageField(upload_to= 'profiles/', blank=True,default="https://drawinglics.com/view/3763785/prosthetic-knowledge-wouldnt-it-be-funny-if-every-facebook-wouldnt-it-be-funny-if-every-facebook-profile-pic-was-this-via.jpg")
    bio = models.TextField(max_length=50, blank=True)
