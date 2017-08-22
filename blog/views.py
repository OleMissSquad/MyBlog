from django.shortcuts import render, get_object_or_404

from .models import Post


# Create your views here.
def index(request):
    return None


def post(request):
    return None


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def year_archive(request):
    return None


def month_archive(request):
    return None


def day_archive(request):
    return None

