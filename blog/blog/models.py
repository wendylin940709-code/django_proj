from django.db import models
from django.urls import reverse

class User(models.Model):
    # 這些欄位必須縮排在 class 裡面
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
   
    # 方法也要縮排在 class 裡面
    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Post(models.Model):
    # 這些欄位必須縮排在 class 裡面
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        #"auth.User",
        User,
        on_delete=models.CASCADE,
    )
    body = models.TextField()  # 這裡要縮排！

    # 方法也要縮排在 class 裡面
    def __str__(self):
        return self.title
