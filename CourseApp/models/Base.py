from django.db import models
from django.utils import timezone


class MyModeBase(models.Model):
    created_date = models.DateTimeField(default=timezone.now())
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
