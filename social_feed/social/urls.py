from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', views.fake_home, name='fake_home'),
]