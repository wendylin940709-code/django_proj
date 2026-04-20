# blog/admin.py
from django.contrib import admin
from .models import Post,User
class PostAdmin(admin.ModelAdmin): # new
    list_display = (
    "title",
    "author",
    "body",
    )
admin.site.register(User) # new
admin.site.register(Post, PostAdmin) # new