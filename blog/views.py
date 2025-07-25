from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Home page – list all posts
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

# Detail page – view one post by ID
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user  # assign author before saving
            form.save()
            return redirect('home')

    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {'form':form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return redirect('post_detail', id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.instance.author = request.user  # assign author before saving
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return redirect('post_detail', id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blog/delete_post.html', {'post': post})
