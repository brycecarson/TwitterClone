from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import PostForm
from .models import Post

# Create your views here.
# def index(request):
#     posts = Post.objects.all()[:20]
#     return render(request,'posts.html',{'posts':posts }) 

def index(request):

    #if the method is post
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
        #if the form is valid
            form.save()
           #if yes save it and redirect it to home
            return HttpResponseRedirect('/')

        #if no then show error
        else:
            return HttpResponseRedirect(form.erros.as_json())
    posts = Post.objects.all().order_by('-created_at')[:50]
    return render(request,'posts.html',{'posts':posts }) 



def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.like == 0:
        post.like += 1
    elif post.like == 1:
        post.like = 0
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.error.as_json())
        
    form = PostForm()
    return render(request, 'edit.html', {'edit': post, 'form': form})

# Create your views here.
