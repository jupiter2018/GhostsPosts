from django.shortcuts import render,reverse,HttpResponseRedirect
from GhostsPosts.models import Boast, Post
from GhostsPosts.forms import PostForm, BoastForm
from django.utils import timezone

def index(request, *args, **kwargs):
    timeNow =  timezone.localtime(timezone.now())
    print(timeNow)
    args = {}
    posts = Post.objects.all().order_by('-created')
    boasts = Boast.objects.all().order_by('-created')

    print(posts)
    if request.GET.get('filterByChoice'):
        featured_filter = request.GET.get('filterByChoice')
        print(featured_filter)
        if(featured_filter=="All"):
            args = {'posts':posts,'boasts':boasts,}
        elif(featured_filter=="Posts") :
            args = {'posts':posts}
        elif(featured_filter=="Boasts"):
            args = {'boasts':boasts}
        elif(featured_filter=="Likes"):
            posts = Post.objects.all().order_by('-postlikes')
            boasts = Boast.objects.all().order_by('-boastlikes')
            args = {'posts':posts,'boasts':boasts,}
       
    else:
        args = {'posts':posts,'boasts':boasts}
    

    
    return render(request,"home.html",{'args':args})


def addPost(request,*args,**kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            Post.objects.create(
                title = data['title'],
                content = data['content'],
                author = data['author'],
            )
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('homepage'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
    
    return render(request,"addPost.html",{'form':form})


def addBoast(request,*args,**kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            Boast.objects.create(
                title = data['title'],
                content = data['content'],
                author = data['author'],
            )
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('homepage'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
    
    return render(request,"addPost.html",{'form':form})


def postLikes(request, id):
    curPost = Post.objects.filter(id=id)
    # .update(postlikes=1)
    numPostLikes = curPost[0].postlikes
    curPost.update(postlikes = numPostLikes+1)
    return HttpResponseRedirect(reverse('homepage'))

def postdisLikes(request, id):
    curPost = Post.objects.filter(id=id)
    # .update(postlikes=1)
    numPostLikes = curPost[0].postlikes
    curPost.update(postlikes = numPostLikes-1)
    return HttpResponseRedirect(reverse('homepage'))
    


def boastLikes(request, id):
    curBoast = Boast.objects.filter(id=id)
    # .update(postlikes=1)
    numBoastLikes = curBoast[0].boastlikes
    curBoast.update(boastlikes = numBoastLikes+1)
    return HttpResponseRedirect(reverse('homepage'))

def boastdisLikes(request, id):
    curBoast = Boast.objects.filter(id=id)
    # .update(postlikes=1)
    numBoastLikes = curBoast[0].boastlikes
    curBoast.update(boastlikes = numBoastLikes-1)
    return HttpResponseRedirect(reverse('homepage'))