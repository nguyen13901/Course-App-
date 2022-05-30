from rest_framework import serializers

from CourseApp.models import LessonView


class LessonViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonView
        fields = ["id", "views", "lesson"]