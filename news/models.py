from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
from time import strftime
from django.urls import reverse
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1024)

    published = models.DateTimeField(default=strftime('%Y-%m-%d %H:%M:%S'))



