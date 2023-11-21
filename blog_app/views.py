from django.shortcuts import render
from blog_app.models import Post, Comment, Category


# Create your views here.
def index(request):
    posts = Post.objects.all().order_by("-created_on")  # the minus tells django with the largest value(newer post)
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


# blog_index() will display a list of all your posts.

def category(request):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,

    }
    return render(request, "blog/category.html", context)


def detail(request, pk):  # pk is the primary key
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,

    }
    return render(request, "blog/detail.html", context)
