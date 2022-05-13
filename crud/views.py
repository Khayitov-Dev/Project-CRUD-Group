from django.shortcuts import render
from crud.models import Post
# Create your views here.

def post_list(request):

    post = Post.objects.all()

    context = {
        'posts':post
    }

    return render(request,'index.html',context)