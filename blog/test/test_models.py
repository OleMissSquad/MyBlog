import datetime

from django.test import TestCase
from django.utils import timezone


from blog.models import *


# Create your tests here.
# Testing on the relational database to see if it works like expected. Test the method create in model class
class UserModelTests(TestCase):
    def test_(self):
        pass


class PostModelTests(TestCase):
    def test_was_published_recently_with_old_post(self):
        """
            was_published_recently() returns False for posts whose date_published
            is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = Post(date_published=time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
            was_published_recently() returns True for posts whose date_published
            is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(date_published=time)
        self.assertIs(recent_post.was_published_recently(), True)

    def test_was_published_recently_with_future_post(self):
        """
            was_published_recently() returns False for posts whose date_published
            is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(date_published=time)
        self.assertIs(future_post.was_published_recently(), False)
