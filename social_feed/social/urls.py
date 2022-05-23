from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'social'

urlpatterns = [
    path('', login_required(views.Dashboard.as_view()), name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='social/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('profile_list/', login_required(views.ProfileList.as_view()), name='profile_list'),
    path('follow_detail/<str:slug>/', login_required(views.FollowDetail.as_view()), name='follow_detail'),
    path('profile_detail/<str:username>/', login_required(views.ProfileDetail.as_view()), name='profile_detail'),
    path('profile_update/<str:slug>/', login_required(views.ProfileUpdate.as_view()), name='profile_update'),
    path('profile_delete/<str:username>/', login_required(views.ProfileInactive.as_view()), name='profile_delete'), #wip
    path('post_delete/<slug:slug>/', login_required(views.PostDelete.as_view()), name='post_delete'),
]
