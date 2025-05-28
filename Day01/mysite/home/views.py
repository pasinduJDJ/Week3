from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import markdown
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def home_view(request):
    last_week = timezone.now() - timedelta(days=7)
    posts = Post.objects.filter(created_at__gte=last_week).order_by('-created_at')
    return render(request, 'home/home.html', {'posts': posts})

def about_view(request):
    return render(request, 'home/about.html')

def blog_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html',{'posts':posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('blog_detail', pk=post.id)  

    return render(request, 'blog/blog_edit.html', {'post': post})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully.')
        return redirect('blog_list')

    return render(request, 'blog/delete_confirm', {'post': post})