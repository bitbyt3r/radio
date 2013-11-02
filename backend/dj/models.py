from django.db import models

class Song(models.Model):
  uploadFilename = models.CharField(max_length=1024)
  filename = models.CharField(max_length=1024)
  title = models.CharField(max_length=512)
  artist = models.CharField(max_length=512)
  length = models.CharField(max_length=64)
  format = models.CharField(max_length=64)
  genre = models.CharField(max_length=512)
  uploadDate = models.DateTimeField()
  approved = models.BooleanField()
  recordDate = models.DateTimeField()
  approvedBy = models.CharField(max_length=128)


