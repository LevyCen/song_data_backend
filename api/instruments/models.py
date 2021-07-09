from django.db import models

from django.utils import timezone


class Instrument(models.Model):
    instrument_id = models.AutoField(primary_key=True)
    instrument = models.TextField(blank=False, null=False)
    created_dt_tm = models.DateTimeField(default=timezone.now)
    updated_dt_tm = models.DateTimeField(auto_now=True)

    class MetaL:
        db_table = 'instruments'
    