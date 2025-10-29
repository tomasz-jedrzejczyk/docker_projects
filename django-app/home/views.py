from django.shortcuts import render
from .models import BlogPost

def index(request):
    # Get the latest published blog posts
    blog_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:5]  # Last 5 posts
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'home/index.html', context)