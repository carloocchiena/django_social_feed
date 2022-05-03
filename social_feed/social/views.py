from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, FormView, UpdateView


from . import models, forms

# Dummy home page to be substituted 
def fake_home(request):
    return render(request, 'social/fake_home.html')


# class Dashboard(View):'
#     """Dashboard view with all posts items for current user"""
#     model = models.Post
#     template_name = 'social/dashboard.html'
    
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {'posts': self.model.objects.all()})
     
    
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

# wip    
class PostForm(FormView):
    """View to create a new post"""
    template_name = 'social/post_form.html'
    form_class = forms.PostForm
    success_url = '/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
