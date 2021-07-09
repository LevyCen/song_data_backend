from django.db import models

from django.utils import timezone


class SimilarBand(models.Model):
    similar_band_id = models.AutoField(primary_key=True)
    song = models.ForeignKey('songs.Song',on_delete=models.DO_NOTHING)
    band = models.ForeignKey('bands.Band',on_delete=models.DO_NOTHING)
    created_dt_tm = models.DateTimeField(default=timezone.now)
    updated_dt_tm = models.DateTimeField(auto_now=True)

    class MetaL:
        db_table = 'similar_bands'
    