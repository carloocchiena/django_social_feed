from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, UpdateView

from . import models, forms

# Main dashboard + post creation view
class Dashboard(View):
    """Dashboard view with all posts items for current user"""
    model = models.Post
    template_name = 'social/dashboard.html'
    
    def get(self, request):
        """Manage posts views for the followed users and the user itself"""
        form = forms.PostForm(request.POST or None)
        user_posts = models.Post.objects.filter(user=request.user).order_by('-created_at')
        follower_posts = models.Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
        posts = user_posts | follower_posts
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
    def post(self, request):
        """Manage posts creation for the user"""
        form = forms.PostForm(request.POST, request.FILES or None)
        user_posts = models.Post.objects.filter(user=request.user).order_by('-created_at')
        follower_posts = models.Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('-created_at')
        posts = user_posts | follower_posts
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('social:dashboard')
            
        return render(request, self.template_name, {'posts': posts, 'form': form})
    
# User registration view
class UserRegistration(View):
    """Manage user registration"""
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
            return redirect('social:profile_update', pk=user.profile.pk)
     
# List of all the profiles
class ProfileList(ListView):
    """View all profiles"""
    model = models.Profile

# View of each profile and follow-unfollow request
class ProfileDetail(View):
    """View details of profile and follow-unfollow request"""
    model = models.Profile
    template_name = 'social/profile_detail.html'
    
    def get(self, request, pk):
        profile = models.Profile.objects.get(pk=pk)
        return render(request, self.template_name, {'profile': profile})
    
    def post(self, request, pk):
        profile = models.Profile.objects.get(pk=pk)
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
        return render(request, self.template_name, {'profile': profile})
    
# View follow-unfollow details of each profile
class FollowDetail(DetailView):
    model = models.Profile
    fields = ['follows', 'followed_by']
    template_name = 'social/follow_detail.html'
    
    def get_profile_followers(self, request, pk):
        profile = models.Profile.objects.get(pk=pk)
        return render(request, template_name, {'profile': profile})
              
# Update user profile
class ProfileUpdateView(UpdateView):
    """View to update user profile"""
    model = models.Profile
    fields = ['bio', 'location', 'birth_date', 'avatar'] # or '__all__'
    success_url = reverse_lazy('social:profile_list') # to be updated to dashboard later

# wip (non usata al momento)   
class PostForm(FormView):
    """View to create a new post"""
    template_name = 'social/profile_form.html'
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
