from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# After you create your model here, run the command:
#     python manage.py makemigrations
#        - this command will create a file, eg: 0001_initial.py
#
#     python manage.py sqlmigrate blog 0001
#         - this command is to see the RAW sql command 

class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    
    class meta:
        ordering = ('-publish',)

    # Django will use this in administration site
    def __str__(self):
        return self.title
