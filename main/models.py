from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    
    class Meta:
        ordering = ['-headline']
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
