from django.db import models
from taggit_selectize.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey("posts.Category", on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey("posts.Author", on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    tags = TaggableManager(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
