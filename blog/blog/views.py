from django.shortcuts import render, get_object_or_404 # new
from .models import Post
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk): # 如果pk存在就傳給post
    post = get_object_or_404(Post, pk=pk) #主健對應的id
    return render(request, "post_detail.html", {"post": post})
