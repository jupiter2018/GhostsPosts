from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length = 30,default="Post")
    author = models.CharField(max_length = 30)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #postlikes = models.ManyToManyField(Author, related_name='postlikes')
    postlikes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}-{self.content}"


class Boast(models.Model):
    title = models.CharField(max_length = 30,default="Boast")
    # author = models.ForeignKey(Author,on_delete=models.CASCADE)
    author = models.CharField(max_length = 30)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # boastlikes = models.ManyToManyField(Author, related_name='boastlikes')
    boastlikes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.title}-{self.content}"



