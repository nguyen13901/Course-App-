from django.db import models

from CourseApp.models import MyModelBase, Course


class Lesson(MyModelBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
