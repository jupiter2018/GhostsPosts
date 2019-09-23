"""GhostsPosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GhostsPosts.models import Post, Boast
from . import views
admin.site.register(Post)
admin.site.register(Boast)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='homepage'),
    path('addpost/',views.addPost,name='addPost'),
    path('addboast/',views.addBoast,name='addBoast'),
    path('postlikes/<int:id>', views.postLikes, name='postLikes'),
    path('postdislikes/<int:id>', views.postdisLikes, name='postdisLikes'),
    path('boastlikes/<int:id>/', views.boastLikes, name='boastLikes'),
    path('boastdislikes/<int:id>/', views.boastdisLikes, name='boastdisLikes'),
    

]
