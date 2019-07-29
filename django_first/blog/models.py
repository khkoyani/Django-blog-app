from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post2(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    # dont do timezone.now() because don't want to execute the function right now.
    # just want to pass the actual function as the default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
    	return self.title

    def get_absolute_url(self):
    	return reverse('post_detail', kwargs={'pk': self.id})