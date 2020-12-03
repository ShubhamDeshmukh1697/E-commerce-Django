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
    post=Blogpost.objects.filter(post_id=blogid)


    return render(request,'blog/blogpost.html',{'post':post[0]})