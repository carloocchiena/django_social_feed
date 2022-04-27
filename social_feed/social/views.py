from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.views import View

from . import models, forms

# Dummy home page to be substituted 
def fake_home(request):
    return render(request, 'social/fake_home.html')

# List of all the profiles
class ProfileList(ListView):
    """View all profiles"""
    model = models.Profile

# View of each profile    
class ProfileDetail(DetailView):
    """View a specific profile"""
    model = models.Profile  
    
# Update user profile
class ProfileUpdateView(UpdateView):
    """View to update user profile"""
    model = models.Profile
    fields = ['bio', 'location', 'birth_date', 'avatar'] # or '__all__'
    success_url = reverse_lazy('social:profile_list') # to be updated to dashboard later

# wip    
class PostForm(FormView):
    """View to create a new post"""
    template_name = 'social/post_form.html'
    form_class = forms.PostForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)