from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel


COMING_UP = 'CU'
STARTING = 'ST'
RUNNING = 'RN'
FINISHED = 'FN'

STATUS = [
    (COMING_UP, 'Coming up'),
    (STARTING, 'Starting'),
    (RUNNING, 'Running'),
    (FINISHED, 'Finished'),
]


class Movie(TimeStampedUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")
    name = models.CharField(max_length=150)
    protagonists = models.CharField(max_length=120)
    poster = models.ImageField()
    start_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default=COMING_UP,
    )
    ranking = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text='1=Poor, 2=Fair, 3=Good, 4=Very Good, Excellent',
        default=0,)