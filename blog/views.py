from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def index(request):
    latest_post_list = Post.objects.order_by("-date_published")[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/index.html', context)


def post(request):
    return None


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def archive(request):
    return HttpResponse("This is the archive page")


def dashboard(request):
    return HttpResponse("This is the dashboard page")


def signup(request):
    return HttpResponse("This is the singup page")


def signin(request):
    return HttpResponse("This is the signin page")


