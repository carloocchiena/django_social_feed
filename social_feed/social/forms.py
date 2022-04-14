from django import forms
from . import models

class Post(forms.ModelForm):
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
        