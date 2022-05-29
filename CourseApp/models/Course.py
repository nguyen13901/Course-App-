from CourseApp.models import MyModelBase, Category
from django.db import models


class Course(MyModelBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ['-id']

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
