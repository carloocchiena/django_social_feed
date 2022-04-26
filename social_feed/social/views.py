from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
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
    
    """
    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['post'] = models.Post.objects.all() # filter(text=self.get_object())
        # ok ora almeno torna tutti i post devo far tornare solo quelli del mio utente
        # è già qualcosa!
        return context
    """
    
# riprendere da qui
class ProfileForm(FormView):
    """View to create a new profile"""
    template_name = 'social/profile_form.html'
    form_class = forms.ProfileForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class PostForm(FormView):
    """View to create a new post"""
    template_name = 'social/post_form.html'
    form_class = forms.PostForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)