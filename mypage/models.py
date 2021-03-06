from __future__ import unicode_literals
from django.contrib import admin
from django.db import models




class Post(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message
        
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'created_at']
    list_display_links = ['title']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'message', 'created_at']
    list_display_links = ['message']
