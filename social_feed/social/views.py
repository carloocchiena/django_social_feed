from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
    
    def get_context_data(self, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        context['post'] = models.Post.objects.all() # filter(text=self.get_object())
        # ok ora almeno torna tutti i post devo far tornare solo quelli del mio utente
        # è già qualcosa!
        return context
    
    
"""
# questo funziona ma la vista è decisamente più lineare vediamo se riesco a costruirla da lì.    
def get_profile(request, pk):
    profile = models.Profile.objects.get(pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'social/profile_detail.html', {'profile': profile})
"""