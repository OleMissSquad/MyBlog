from django.conf.urls import url

from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    # e.g: blog/123/detail
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    # e.g: blog/post
    url(r'^post/$', views.post, name='post'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
]
