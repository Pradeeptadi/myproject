from django.shortcuts import render, get_object_or_404
from blog.models import Post
  # Adjust if model import differs

def home(request):
    return render(request, "home.html")

def page(request):
    return render(request, "page.html")


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
