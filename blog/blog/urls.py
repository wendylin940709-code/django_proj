from django.urls import path
from .views import post_list, post_detail 

#網址後是空的會直接call post_list這個view
#<int:pk>放pk的index，並讓post_detail去接收
urlpatterns = [
path("post/<int:pk>/", post_detail, name="post_detail"), # new
path("", post_list, name="home"),
]
