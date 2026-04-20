from django.contrib import admin
from django.urls import path, include # include建立的blog/urls
urlpatterns = [
path("admin/", admin.site.urls),
path("", include("blog.urls")), # new
]

