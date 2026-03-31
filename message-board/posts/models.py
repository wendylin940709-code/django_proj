from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] # 顯示前50個字，方便管理後台閱讀