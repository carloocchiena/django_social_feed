from django import forms
from . import models

# da testare
class ProfileEditForm(forms.ModelForm):
    """Manage user creation"""
    class Meta:
        model = models.Profile
        fields = ['bio', 'location', 'birth_date', 'avatar'] # or '__all__'
        
class PostForm(forms.ModelForm):
    """Manage post creation"""
    class Meta:
        model = models.Post
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={
                'label': '',
                'class': 'form-control',
                'name': 'post_text',
                'id': 'post_text',
                'rows': 4, 
                'cols': 40, 
                'placeholder': 'What\'s happening?',
                'required': True
                                          },
            ),
            'image': forms.FileInput(attrs={
                'label': '',
                'class': 'form-control',
                'name': 'post_img',
                'id': 'post_img',
                'placeholder': 'Upload a picture!',
                'onchange': 'document.getElementById("imageBox").src = window.URL.createObjectURL(this.files[0])',
             }
            )
        }
        