from django.db import models

from helpers.models import BaseModel


class Event(BaseModel):
    """Tadbirlar uchun model"""

    title = models.CharField('Nomi', max_length=150)
    slug = models.SlugField('Slugi', max_length=150)
    place_name = models.CharField('Joy nomi', max_length=250)
    date = models.DateField('Sanasi')
    description = models.TextField('Tavsifi')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tadbir'
        verbose_name_plural = 'Tadbirlar'