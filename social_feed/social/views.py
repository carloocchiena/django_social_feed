from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView

from . import models, forms
from .coins_data import plus_coins, minus_coins

class Dashboard(View):
    """Dashboard view with all posts items for current user.
    GET return list of posts in ascending order from user followed by the user and user itself.
    POST add a post from logged user and add 15 coins.
    """
    model = models.Post
    template_name = 'social/dashboard.html'
    
    def get(self, request):
        """Return posts views for the followed users and the user itself"""
        form = forms.PostForm(request.POST or None)
        user_posts = models.Post.objects.filter(user=request.user)
        follower_posts = models.Post.objects.filter(user__profile__in=request.user.profile.follows.all())
        posts = user_posts | follower_posts
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
    def post(self, request):
        """Manage posts creation for the user"""
        form = forms.PostForm(request.POST, request.FILES or None)
        user_posts = models.Post.objects.filter(user=request.user)
        follower_posts = models.Post.objects.filter(user__profile__in=request.user.profile.follows.all())
        posts = user_posts | follower_posts
        coins = models.Profile.objects.get(user=request.user).coins 
        current_user_profile = request.user.profile 
        if form.is_valid():
            current_user_profile.coins += plus_coins 
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            current_user_profile.save() 
            return redirect('social:dashboard')
            
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
class UserRegistration(View):
    """Manage user registration.
    GET render the form.
    POST create a new user, logs it, and redirect to the user's profile.
    """
    model = models.Profile
    template_name = 'social/register.html'
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('social:profile_update', slug=user.profile.user)
        else:
            return render(request, self.template_name, {'form': form})
     
class ProfileList(ListView):
    """View all profiles"""
    model = models.Profile

class ProfileDetail(View):
    """View details of profile and follow-unfollow request.
    GET return the profile details.
    POST manage follow-unfollow request.
    """
    model = models.Profile
    template_name = 'social/profile_detail.html'
    
    def get(self, request, username):
        # profile = models.Profile.objects.get(pk=pk)
        profile = get_object_or_404(models.Profile, user__username=self.kwargs['username'])
        return render(request, self.template_name, {'profile': profile})
    
    def post(self, request, username):
        # profile = models.Profile.objects.get(pk=pk)
        profile = get_object_or_404(models.Profile, user__username=self.kwargs['username'])
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
        return render(request, self.template_name, {'profile': profile})
    
class FollowDetail(DetailView):
    """Display followers and following."""
    model = models.Profile
    fields = ['follows', 'followed_by']
    slug_field = "user__username"
    template_name = 'social/follow_detail.html'
    
    def get_profile_followers(self, request, username):
        profile = get_object_or_404(models.Profile, user__username=self.kwargs['username'])
        return render(request, template_name, {'profile': profile})
              
class ProfileUpdate(UpdateView):
    """View to update user profile."""
    model = models.Profile
    form_class = forms.ProfileEditForm
    slug_field = "user__username"
    template_name_suffix = '_update'
    success_url = reverse_lazy('social:dashboard')
    
    # User can updates only his\her profile, or get a 404 error
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)       
    
class ProfileInactive(View):
    """User can made its profile unactive"""
    model = models.Profile
    template_name = 'social/profile_delete.html'
      
    def get(self, request, username):
        """Users can deactivate only their profile, or get a 404 error"""
        owner = self.request.user
        profile = get_object_or_404(models.Profile, user__username=self.kwargs['username'])
        if owner == profile.user:
            return render(request, self.template_name, {'profile': profile})
        else:
            raise Http404
    
    def post(self, request, username):
        """Deactivate user profile and update its username"""
        owner = self.request.user
        profile = request.user.profile
        if owner == profile.user:
            owner.is_active = False
            profile.is_active = False
            owner.username = f"{owner.username}_deactivated"
            owner.save()
            profile.save()
            logout(request)
        else:
            raise Http404
        return redirect('social:register')
           
class PostDelete(DeleteView):
    """Delete a post for logged user"""
    model = models.Post
    slug_field = "id"
    # success_url = reverse_lazy('social:dashboard')
        
    # Users can delete only their posts, or get a 404 error
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
    
    # remove 10 coins if post is deleted
    def get_success_url(self):
        user = self.request.user
        current_user_profile = self.request.user.profile 
        coins = models.Profile.objects.get(user=user).coins 
        current_user_profile.coins -= minus_coins 
        current_user_profile.save() 
        return reverse('social:dashboard')
    
class Help(View):
    """Help page"""
    template_name = 'social/help.html'
    
    def get(self, request):
        return render(request, self.template_name)
