from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Post
from django.utils import timezone 
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #posts=Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form_obj= form.save(commit=False)
            form_obj.auther = request.user
            form_obj.published_date = timezone.now()
            form_obj.save()
            return redirect('post_detail',pk=form_obj.pk)
        return render(request,'blog/post_new.html',{'form':form_obj})   ### this line want to explain
    else:
        form= PostForm()
        return render(request,'blog/post_new.html',{'form':form})     ### this line also




