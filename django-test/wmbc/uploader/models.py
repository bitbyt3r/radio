from django.db import models

class Song(models.Model):
  name = models.CharField(max_length=512)
  publishDate = models.DateTimeField('date published')
  artist = models.CharField(max_length=256)

class Artist(models.Model):
  name = models.CharField(max_length=256)

