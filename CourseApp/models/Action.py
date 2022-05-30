from CourseApp.models import ActionBase
from django.db import models


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart'),
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


