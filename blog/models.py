from django.db import models
from django.utils import timezone


import datetime

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=18)
    password = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    description = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False);
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name;


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    is_enabled = models.BooleanField()
    date_created = models.DateTimeField()

    def __str__(self):
        return self.name;


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=144)
    post_content = models.TextField(blank=True)
    date_published = models.DateTimeField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0);
    comment_enabled = models.BooleanField(default=True);
    is_enabled = models.BooleanField()
    category = models.ManyToManyField(Category, through='PostCategory')

    # Storing file maybe???
    #file = models.FileField();

    def __str__(self):
        return self.post_title;

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_published <= now


class PostCategory(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return Post.objects.get(pk=self.post_id).__str__() + ", " + Category.objects.get(pk=self.category_id).__str__()


class BookmarkedPost(models.Model):
    id = models.AutoField(primary_key=True, default=0)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return Post.objects.get(pk=self.post_id).__str__() + ", " + User.objects.get(pk=self.user_id).__str__()


class Comment(models.Model):
    id = models.AutoField(primary_key=True, default=0)

    # Needs to work on how to reply to a comment on a post
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    #is_reply_to_id = models.

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField()
    comment = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)
    is_enabled = models.BooleanField()

    def __str__(self):
        return self.id
