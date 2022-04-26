from django import forms
from . import models

# da testare
class ProfileForm(forms.ModelForm):
    """Manage user creation"""
    class Meta:
        model = models.Profile
        fields = ['bio', 'location', 'birth_date', 'avatar']
        
class PostForm(forms.ModelForm):
    """Manage post creation"""
    class Meta:
        model = models.Post
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 
                                          'cols': 40, 
                                          'placeholder': 'What\'s happening?'
                                          },
            )
        }
        