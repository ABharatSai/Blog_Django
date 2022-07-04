from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class tempManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    choice = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=250)  # Title
    slug = models.SlugField(
        max_length=250, unique_for_date='date')  # Link or URLs
    date = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=choice, default='draft')
    objects = models.Manager()
    newmanager = NewManager()  # for published change in views
    tempManage = tempManager()  # For drafts chanfge in views
    image = models.ImageField(upload_to="images/", default="images/temp.jpg")

    def get_absolute_url(self):
        return reverse("home:single", args=[self.slug])

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
