from django.shortcuts import render

from gram.models import Post, Profile
from .forms import NewPostForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def profile(request,user_id=None):
    if user_id == None:
        user_id=request.user.id
    current_user = User.objects.get(id = user_id)
    # user = current_user
    images = Post.objects.filter(user=current_user)
    profile = Profile.objects.all()
    followers = len(Follow.objects.followers(current_user))
    following = len(Follow.objects.following(current_user))
    return render(request, 'profile.html', locals())


# Create your views here.
