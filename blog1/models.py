from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(max_length=150, unique=True)
    body=models.TextField(blank=True,db_index=True)
    date_pub=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    tags=models.ManyToManyField('Tag',blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('post_detail_url',kwargs={'slug':self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Tag(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return '{}'.format(self.title)