from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()


class Song(models.Model):
    artiste_id = models.OneToOneField(Artiste, on_delete=models.CASCADE)
    artistes = models.ForeignKey(Artiste, related_name='artiste', on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=0)


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_artistes = models.OneToOneField(Song, related_name='song_artiste', on_delete=models.CASCADE)
    content = models.CharField(max_length=2000)
