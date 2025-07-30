from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')  # Fetch all posts from the database
    return render(request, 'posts/posts_list.html', {'posts': posts})


def posts_page(request, slug):
    posts = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': posts})

   


