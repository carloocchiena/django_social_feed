from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', views.fake_home, name='fake_home'),
    path('profile_list/', views.ProfileList.as_view(), name='profile_list'),
    path('profile_detail/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile_form/', views.ProfileForm.as_view(), name='profile_form'),
    path('post_form/', views.PostForm.as_view(), name='post_form'),
]