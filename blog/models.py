from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    title   = models.CharField(max_length=220)
    slug    = models.SlugField(unique_for_date='publish', max_length=220)
    author  = models.CharField(User,  max_length=150)
    body    = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status  = models.CharField(max_length=10, choices= STATUS_CHOICES, default='draft')


    class Meta():
        ordering = ['-publish']

    def __str__(self):
        return self.title
