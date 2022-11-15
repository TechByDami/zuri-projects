from django.db import models
from datetime import datetime


class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    title = models.CharField(max_length=256)
    date_released = models.DateField(default=datetime.today)
    likes = models.IntegerField(default=0)
    artist_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return self.content

