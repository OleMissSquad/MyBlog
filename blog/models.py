from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=18)
    password = models.CharField(max_length=40)
    email = models.EmailField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    description = models.TextField()
    is_admin = models.BooleanField(default=False);
    is_blocked = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=45)
    is_enabled = models.BooleanField()
    date_created = models.DateTimeField()


class Post(models.Model):
    post_title = models.CharField(max_length=144)
    post_content = models.TextField()
    date_published = models.DateTimeField()
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0);
    comment_enabled = models.BooleanField();
    is_enabled = models.BooleanField()

    # Storing file maybe???
    #file = models.FileField();


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class BookmarkedPost(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    # Needs to work on how to reply to a comment on a post
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    #is_reply_to_id = models.

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField()
    comment = models.TextField()
    is_read = models.BooleanField(default=False)
    is_enabled = models.BooleanField()
