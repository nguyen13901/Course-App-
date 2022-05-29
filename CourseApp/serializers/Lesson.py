from rest_framework import serializers

from CourseApp.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'created_date', 'updated_date', 'course']
