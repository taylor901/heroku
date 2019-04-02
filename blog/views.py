from django.shortcuts import render
from .models import Post

def post_list(request):
    # This is a QuerySet that returns all the posts ordered by the publish date
    posts = Post.objects.order_by('published_date')
    # Pass the posts to the template
    return render(request, 'blog/post_list.html', {'posts': posts})
# Create your views here.
