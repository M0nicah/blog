from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:  # this controls the plural name of the class
        verbose_name_plural = "Categories"  # verbose is for adding the correct spelling in the django admin page

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")  # assign many categories to many posts

    def __str__(self):
        return self.title  # this will help admin know what blog post they're looking for


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)  # many comments can be assigned to one post.

    def __str__(self):
        return f"{self.author} on '{self.post}'"
