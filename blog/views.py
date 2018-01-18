from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from blog.models import Post


def index(request):
    posts = list(Post.objects.all())
    """ page = request.GET.get('page')
    try:
        posts_nav = Paginator.page(page)
    except PageNotAnInteger:
        posts_nav = Paginator.page(1)
    except EmptyPage:
        posts_nav = Paginator.page(Paginator.num_pages)
    """
    return render(request, 'blog/index.html', { 'blogs': posts})


def detail(request, year=2017, month=1, day=15, post='love'):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    return render(request, 'blog/detail.html', {'post': post})


def Notfound(request):
    return render(request, 'blog/404.html')






