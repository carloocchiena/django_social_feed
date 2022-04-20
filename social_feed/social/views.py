from django.shortcuts import render
from django.views.generic import ListView


from . import models, forms

# Create your views here.
def fake_home(request):
    return render(request, 'social/fake_home.html')

# here
class Profile(ListView):
    model = models.Profile

    # template_name = 'social/profiles_list.html'
    
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['profiles'] = models.Profile.objects.all()
        # return context