from django.shortcuts import render
from .models import Blogpost
from django.http import request,HttpResponse
# Create your views here.
def index(request):
    # show all blog posts here and show selected in blogPost page
    blogs=Blogpost.objects.all()
    params={'blogs':blogs}
    return render(request,'blog/index.html',params)

def blogPost(request,blogid):
    params={}
    allPosts=Blogpost.objects.all()

    for i in allPosts:
        if i.post_id==blogid:
            params['post']=i
        else:
            if(i.post_id==(blogid+1)):
                params['next']=i
            elif(i.post_id==(blogid-1)):
                params['prev']=i
            else:
                pass
    
    print(params)
    # post=Blogpost.objects.filter(post_id=blogid)

    return render(request,'blog/blogpost.html',params)