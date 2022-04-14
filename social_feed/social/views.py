from django.shortcuts import render

from . import models, forms

# Create your views here.
def fake_home(request):
    return render(request, 'social/fake_home.html')