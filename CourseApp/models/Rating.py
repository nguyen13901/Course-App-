from django.db import models

from CourseApp.models import ActionBase


class Rating(ActionBase):
    rate = models.PositiveSmallIntegerField(default=0)
