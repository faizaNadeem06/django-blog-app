from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView
from . models import *
from form import *


# def home(request):
#     return render(request,'home.html',{})


def Homeview(request):
    post=Post.objects.all()
    return render(request,'home.html',{'Post':post})

def Createpost(request):
    form=postform()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(Homeview)
    else:
        form=postform()

    return render(request,'addpost.html',{'form':form})

# def Createpost(request):
#     return render(request,'addpost.html',fields='__all__')

# def Detailpost(request):
#     return render(request, "details.html", DetailView)


# class Homeview(ListView):
#     model = Post
#     template_name='home.html


# class Detailpost(DetailView):
#     model = Post
#     template_name = 'details.html'

# class Createpost(CreateView):
#     model = Post
#     template_name = 'addpost.html'
#     fields='__all__'
    

# class update_post(UpdateView):
#     model=Post
#     template_name='update_post.html'
#     fields=['title','body']



# Create your views here.
