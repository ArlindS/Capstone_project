from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# python3 manage.py makemigrations
# python3 manage.py sqlmigrate academia 0001 --> this command shows sql code
# Run --> python3 manage.py migrate --> to finalize making changes to db


class ResourceCS(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceTh(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceDs(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceCe(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceAlg(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceAlg_Graphs(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link


class ResourceGraphs(models.Model):
    link = models.URLField(("link"), max_length=500)

    def __str__(self):
        return self.link
