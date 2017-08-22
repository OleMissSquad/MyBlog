from django.db import models


# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_date = models.DateTimeField("Date Posted")

    # May use TextField with no max length or charField with max_length enforce in database
    post_content = models.CharField()

