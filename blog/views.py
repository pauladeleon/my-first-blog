from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})# Create your views here.
from django.shortcuts import render
from .models import Post
