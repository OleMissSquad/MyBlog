from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    # e.g: blog/index
    url(r'^index/$', views.index, name='index'),
    # e.g: blog/123/detail
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # e.g: blog/post
    url(r'^post/$', views.post, name='post'),
]
