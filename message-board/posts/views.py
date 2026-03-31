# from django.views.generic import ListView
# from .models import Post

# class PostListView(ListView):
#     model = Post
#     template_name = "post_list.html"

from django.views.generic import ListView # 新增
from .models import Post

class PostList(ListView): # 新增
    model = Post
    template_name = "post_list.html"
    def get_queryset(self):
        # 這裡的邏輯就相當於您在 Shell 裡練習的指令
        return Post.objects.filter(text__contains="What")