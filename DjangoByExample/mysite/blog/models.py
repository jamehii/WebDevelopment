from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# After you create your model here, run the command:
#     python manage.py makemigrations
#        - this command will create a file, eg: 0001_initial.py
#
#     python manage.py sqlmigrate blog 0001
#         - this command is to see the RAW sql command 
#         - by default, django will create databaes table based on your :
#            AppName_ModelName ==> blog_post ( CREATE TABLE "blog_post")
#         - to customize your own table name, you can use attribute "db_table" in meta class
#     By default, Django create PRIMARY KEY for you, but you can specify your own by:
#         using primary_key=True in your model "field"
#


# objects = default manager for all database
#     we can define custom manager like below 

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


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
    
    # default manager
    objects = models.Manager()

    # custom manager
    published = PublishedManager()

    class meta:
        ordering = ('-publish',)

    # Django will use this in administration site
    def __str__(self):
        return self.title
