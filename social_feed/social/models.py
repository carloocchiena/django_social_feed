from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    """ Create user profiles and manage their attributes"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) # to be checked
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', null=True, blank=True) # to be checked
    
    def __str__(self):
        return (f'{self.user.username}'
                f'{self.created_at:%Y-%m-%d %H:%M}'
                f'{self.text[:150]}...'
                f'{self.image}')
