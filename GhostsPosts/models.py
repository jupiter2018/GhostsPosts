from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    
    
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length = 30,default="Post")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}-{self.content}"


class Boast(models.Model):
    title = models.CharField(max_length = 30,default="Boast")
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}-{self.content}"
