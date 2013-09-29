#!/usr/bin/python
from uploader.models import Song
from uploader.models import Artist
from django.contrib import admin

admin.site.register(Song)
admin.site.register(Artist)
