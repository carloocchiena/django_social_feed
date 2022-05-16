from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView

from . import models, forms

class Dashboard(View):
    """Dashboard view with all posts items for current user.
    GET return list of posts in ascending order from user followed by the user and user itself.
    POST add a post from logged user.
    """
    model = models.Post
    template_name = 'social/dashboard.html'
    
    def get(self, request):
        """Manage posts views for the followed users and the user itself"""
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
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('social:dashboard')
            
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
class UserRegistration(View):
    """Manage user registration.
    GET render the form.
    POST create a new user and redirect to the user profile.
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
    slug_field = "user__username"
    fields = ['bio', 'location', 'birth_date', 'avatar'] # or '__all__'
    success_url = reverse_lazy('social:dashboard')
    
    # User can updates only his\her profile, or get a 404 error
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)
    
class PostDelete(DeleteView):
    """Delete a post for logged user"""
    model = models.Post
    slug_field = "id"
    success_url = reverse_lazy('social:dashboard')
    
    # Users can delete only their posts, or get a 404 error
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)  

# wip (non usata al momento)   
class PostForm(FormView):
    """View to create a new post"""
    template_name = 'social/profile_form.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
