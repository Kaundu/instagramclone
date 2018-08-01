from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),    url('^$',views.index,name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),    url('^$',views.index,name = 'index'),
    url(r'^new/post$', views.new_post, name='new-post'),    url(r'^profile/(?P<user_id>\d+)?$', views.profile, name='profile'),