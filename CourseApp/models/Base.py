from django.db import models
from django.utils import timezone


class MyModelBase(models.Model):
    subject = models.CharField(max_length=200, null = False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.subject
