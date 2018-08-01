from django import forms
from .models import *

class NewPostForm(forms.ModelForm):
    class Meta :
        model = Post
        exclude = ['user', 'post_date','liker']
