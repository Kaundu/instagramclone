from django.shortcuts import render

from gram.models import Post, Profile
from .forms import NewPostForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', locals())



# Create your views here.
