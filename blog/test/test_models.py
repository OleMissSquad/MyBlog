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
    def test_was_published_recently_with_future_post(self):
        """
            was_published_recently() returns False for posts whose pub_date
            is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(date_published=time)
        self.assertIs(future_post.was_published_recently(), False)
