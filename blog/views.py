from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from blog.models import Post
#from blog.forms import PostForm
import time

# Create your views here.
def post_list(request):
    time.sleep(10)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
