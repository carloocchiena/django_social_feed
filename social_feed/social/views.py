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

"""
# questo funziona ma la vista è decisamente più lineare vediamo se riesco a costruirla da lì.    
def get_profile(request, pk):
    profile = models.Profile.objects.get(pk=pk)
    if request.method == 'POST':
        pass
    return render(request, 'social/profile_detail.html', {'profile': profile})
"""