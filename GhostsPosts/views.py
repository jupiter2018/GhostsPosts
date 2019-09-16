from django.shortcuts import render,reverse,HttpResponseRedirect
from GhostsPosts.models import Boast, Post, Author
from GhostsPosts.forms import PostForm, BoastForm

def index(request, *args, **kwargs):
    args = {}
    posts = Post.objects.all().order_by('-created')
    boasts = Boast.objects.all().order_by('-created')
    # print(posts)
    if request.GET.get('filterBy'):
        featured_filter = request.GET.get('filterBy')
        # query = Unit.listType.filter(unitType=featured_filter)
        print(featured_filter)
        if(featured_filter=="All"):
            args = {'posts':posts,'boasts':boasts}
        elif(featured_filter=="Posts") :
            args = {'posts':posts}
        elif(featured_filter=="Boasts"):
            args = {'boasts':boasts}

    else:
        args = {'posts':posts,'boasts':boasts}
    
    return render(request,"home.html",args)


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