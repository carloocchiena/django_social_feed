from django import forms
from . import models

class ProfileEditForm(forms.ModelForm):
    """Manage user creation"""
    class Meta:
        model = models.Profile
        fields = ['bio', 'location', 'birth_date', 'avatar'] # or '__all__'
        widgets = {
            'bio': forms.Textarea(attrs={
                'label': 'Bio',
                'class': 'form-control',
                'name': 'user_bio',
                'id': 'user_bio',
                'rows': 4, 
                'cols': 40, 
                'placeholder': 'That\'s you!',
                'required': False,
                },
            ),
            'location': forms.TextInput(attrs={
                'label': 'Location',
                'class': 'form-control',
                'name': 'user_location',
                'id': 'user_location',
                'placeholder': 'Where are you from?',
                'required': False,
                },
            ),
             'birth_date': forms.DateInput(attrs={
                'label': 'Birth date',
                'class': 'form-control',
                'name': 'user_birth_date',
                'id': 'user_birth_date',
                'placeholder': 'dd/mm/yyyy',
                'required': False, 
                 },
            ),   
             'avatar': forms.FileInput(attrs={
                'label': 'Avatar',
                'class': 'form-control',
                'name': 'user_avatar',
                'id': 'user_avatar',
                'placeholder': 'Upload a picture!',
                'onchange': 'document.getElementById("imageBox").src = window.URL.createObjectURL(this.files[0])',
                'required': False,
                },
            ),
        }
        
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
                'required': True,
                },
            ),
            'image': forms.FileInput(attrs={
                'label': '',
                'class': 'form-control',
                'name': 'post_img',
                'id': 'post_img',
                'placeholder': 'Upload a picture!',
                'onchange': 'document.getElementById("imageBox").src = window.URL.createObjectURL(this.files[0])',
             },
            ),
        }
        