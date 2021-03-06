from django.db import models
from django.db.models import signals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    """Create user profiles and manage their attributes"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=180, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='social/static/social/avatars/', null=True, blank=True) 
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    coins = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# Signal function to create a profile when a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # if you want the new user is also following him/herself add:
        # user_profile.follows.add(instance.profile)
        # user_profile.save()
        
class Post(models.Model):
    """Create post model and manage its attributes""" 
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    text = models.TextField(max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='social/static/social/posts/', null=True, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return (f'{self.user.username} '
                f'{self.created_at:%Y-%m-%d %H:%M} '
                f'{self.text[:20]}...')
