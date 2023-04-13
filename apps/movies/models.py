from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel


COMING_UP = 'CU'
STARTING = 'ST'
RUNNING = 'RN'
FINISHED = 'FN'

STATUS = [
    (COMING_UP, _('Coming up')),
    (STARTING, _('Starting')),
    (RUNNING, _('Running')),
    (FINISHED, _('Finished')),
]


class Movie(TimeStampedUUIDModel):
    name = models.CharField(max_length=250)
    protagonists = models.CharField(max_length=250)
    poster = models.ImageField()
    start_date = models.DateTimeField()
    status = models.CharField(
        max_length=250,
        choices=STATUS,
        default=COMING_UP,
    )
    ranking = models.IntegerField(verbose_name=_("Ranking"), default=0,)
    
    def __str__(self):
        return self.name