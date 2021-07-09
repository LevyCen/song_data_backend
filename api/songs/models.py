from django.db import models

from django.utils import timezone


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song = models.TextField(blank=False, null=False)
    duration = models.DurationField()
    date = models.DateTimeField()
    album = models.ForeignKey('albums.Album',on_delete=models.DO_NOTHING)
    band = models.ForeignKey('bands.Band',on_delete=models.DO_NOTHING)
    artist = models.ForeignKey('artists.Artist',on_delete=models.DO_NOTHING)
    genre = models.ForeignKey('genres.Genre',on_delete=models.DO_NOTHING)
    subgenre = models.ForeignKey('subgenres.Subgenre',on_delete=models.DO_NOTHING)
    created_dt_tm = models.DateTimeField(default=timezone.now)
    updated_dt_tm = models.DateTimeField(auto_now=True)

    class MetaL:
        db_table = 'songs'
    