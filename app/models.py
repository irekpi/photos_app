from django.db import models
from photos_mng.settings import DATABASES


class Photo(models.Model):
    """
    Basic model representing Photo in DB
    """
    photo_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Title", max_length=100)
    album_id = models.PositiveIntegerField(verbose_name="Album ID")
    url = models.URLField(verbose_name="URL", max_length=200, default=f"sqlite:///{DATABASES['default']['NAME']}")
    width = models.IntegerField(verbose_name="Width", blank=True, default=0)
    height = models.IntegerField(verbose_name="Height", blank=True, default=0)
    main_color = models.CharField(verbose_name="Dominant Color", max_length=20, blank=True, null=True)

    class Meta:
        ordering = ['photo_id']
